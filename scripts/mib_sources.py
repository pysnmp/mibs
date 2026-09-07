#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Provenance for the MIB text checked into ``src/``.

Every module under ``src/`` came from somewhere. For most of this
repository's life that somewhere was not written down: MIBs arrived in
bulk from the snmplabs and librenms collections, were hand-repaired when
they would not compile, and the repair and the import blurred into one
another in the file. A copy eight years behind its publisher and a copy
carrying a deliberate one-line fix look exactly alike on disk.

This module is the machinery for taking that apart, using the same shape
pysmi uses for the base MIBs it bundles (``scripts/update_bundled_mibs.py``
there):

    checked-in text == publisher's text + our patch

``mib-sources.json`` names the publisher for each module it covers, and
``scripts/mib-patches/`` holds the patch where we have one. A module with
a source and no patch must match its publisher byte for byte; one with a
patch must match the publisher's text with that patch applied. Either way
the vendor's own text is the baseline, our change is separately readable,
and ``update_vendor_mibs.py --check`` can say every month whether the
publisher has moved.

What this cannot recover
------------------------

A patch can only be reconstructed against text we can still fetch, and
attributed only to a change we can still see. Neither holds everywhere:

- A module whose publisher serves nothing fetchable -- no public URL, or
  only behind a support login -- has no baseline to diff against, so it
  stays unmanaged and is simply listed as such.
- An edit made to a MIB *before* it reached this repository is invisible.
  The snmplabs and librenms collections were themselves hand-repaired for
  years, and those repairs arrived here inside the imported file. Nothing
  in our git history distinguishes them from the vendor's own bytes.

So adopting a source turns a silently-patched file into a visibly-patched
one only for edits made since the import. Older repairs stay silent, and
the first ``--check`` against a newly adopted source is what surfaces them
-- as a divergence nobody can attribute. That is a real limit of the
approach, not a gap to be closed later.
"""

from __future__ import annotations

import difflib
import io
import json
import pathlib
import re
import subprocess
import threading
import time
import urllib.error
import urllib.request
import zipfile
from typing import Any, Iterable, Iterator

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
MANIFEST = ROOT / "mib-sources.json"
PATCHES = HERE / "mib-patches"
SRC = ROOT / "src"

#: How a fetch is retried. A monthly sweep makes upwards of a thousand
#: requests to one host, so a single refused connection must not be read
#: as a vendor having withdrawn a module.
ATTEMPTS = 3
BACKOFF = 2.0
TIMEOUT = 60


class Unreachable(Exception):
    """A publisher could not be reached, as opposed to having changed.

    Kept distinct from every other failure so that a sweep can say
    "the vendor moved" and "the network was down" in different words.
    """


class NotAModule(Exception):
    """A fetch succeeded but did not return the MIB module it should have.

    A vendor that has put its download behind a bot check or a login
    answers 200 with an HTML page. Comparing that against a MIB reports
    drift on every module the source covers, and adopting it would
    replace real MIB text with the interstitial.
    """


def load_manifest() -> dict[str, Any]:
    """Read ``mib-sources.json``."""
    return json.loads(MANIFEST.read_text())


def save_manifest(manifest: dict[str, Any]) -> None:
    """Write ``mib-sources.json`` back, sorted so diffs stay readable."""
    text = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    MANIFEST.write_text(text)


def download(url: str) -> bytes:
    """Read one URL, retrying a connection that simply failed.

    Raises:
        Unreachable: every attempt failed, or the server answered 5xx.
    """
    last: Exception | None = None

    for attempt in range(ATTEMPTS):
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT) as response:  # noqa: S310
                data: bytes = response.read()
            return data
        except urllib.error.HTTPError as exc:
            if exc.code < 500:
                raise Unreachable(f"{url}: HTTP {exc.code}") from exc
            last = exc
        except Exception as exc:  # noqa: BLE001
            last = exc

        if attempt + 1 < ATTEMPTS:
            time.sleep(BACKOFF * (attempt + 1))

    raise Unreachable(f"{url}: {last}")


#: One lexer per thread. PLY lexers carry position state, and a sweep
#: runs its fetches in parallel.
_lexers = threading.local()


def _lexer() -> Any:
    """The ASN.1 lexer this thread reads MIB text with.

    Built for the relaxed SMIv1 dialect, which is what ``mibdump``
    compiles this repository with, so a module this accepts is one the
    build will go on to accept too.
    """
    existing = getattr(_lexers, "lexer", None)

    if existing is None:
        from pysmi.lexer.smi import lexerFactory
        from pysmi.parser.dialect import smiV1Relaxed

        existing = lexerFactory(**smiV1Relaxed)()
        _lexers.lexer = existing

    return existing


def _tokens(data: bytes) -> Iterator[Any]:
    """Lex *data*, yielding tokens until it ends or stops making sense.

    Text that stops lexing partway still yields what came before. Vendor
    MIB text is not uniformly clean, and a stray byte deep inside a
    module says nothing about whether the file is one.
    """
    lexer = _lexer()
    lexer.reset()
    lexer.lexer.input(data.decode("utf-8", "replace"))

    while True:
        try:
            token = lexer.lexer.token()
        except Exception:  # noqa: BLE001 - a lexer error just ends the scan
            return

        if token is None:
            return

        yield token


#: What a module name can be lexed as. Upper case is the convention and
#: very nearly universal, but a handful of vendors here ship a module
#: named ``companyMIB`` or ``proware-SNMP-MIB``, which the lexer hands
#: back as a lower-case identifier. They compile; refusing to recognise
#: them would only mean this could never check them.
NAME_TOKENS = ("UPPERCASE_IDENTIFIER", "LOWERCASE_IDENTIFIER")


def module_names(data: bytes) -> list[str]:
    """Every module *data* declares a header for.

    Lexed with pysmi's own lexer rather than matched with an expression
    of our own. A module header is not written on one line as often as
    one would like -- vendors break it across lines and drop a
    ``-- REVISION`` note into the middle of it -- and the lexer already
    knows how ASN.1 comments and line breaks work. This repository
    depends on pysmi to compile these files; a second, worse idea of
    what a MIB looks like would only be one more thing to be wrong.

    Used to tell a MIB from whatever a vendor's CDN serves once its
    download has moved behind a bot check or a login: those answer 200
    with an HTML page, which the lexer rejects on the first ``<``.
    """
    found: list[str] = []
    previous: str | None = None

    for token in _tokens(data):
        if token.type == "DEFINITIONS" and previous is not None:
            found.append(previous)
        if token.type in NAME_TOKENS:
            previous = token.value
        else:
            previous = None

    return found


def require_module(data: bytes, expected: str) -> bytes:
    """Return *data* if it really is the MIB module *expected*.

    Raises:
        NotAModule: it declares no module, or not the one asked for. The
            first is a login wall or an error page served as 200. The
            second is a source whose layout has moved underneath us --
            Cisco reissuing a module under a new name at the old path,
            say, which adopted blindly would replace a module that every
            importer still asks for by its old name.
    """
    found = module_names(data)

    if not found:
        head = data[:120].decode("utf-8", "replace").strip()
        raise NotAModule(f"served no MIB module (starts {head[:80]!r})")

    if expected not in found:
        raise NotAModule(f"served {', '.join(found)}, not {expected}")

    return data


def revision_of(data: bytes) -> str:
    """The newest MODULE-IDENTITY revision in *data*, as ``YYYY-MM-DD``.

    ``--`` for a module carrying none, which is normal for SMIv1 text.
    Read off the tokens rather than out of a parsed module, because a
    file too broken to compile still has to answer this -- it is what a
    human is shown when deciding whether a copy has fallen behind.

    From the lexer for the same reason as the module name: a
    ``LAST-UPDATED`` written inside a DESCRIPTION is prose, and only
    something that knows ASN.1 strings from ASN.1 keywords can tell the
    difference.
    """
    stamps: list[str] = []
    expecting = False

    for token in _tokens(data):
        if token.type in ("LAST_UPDATED", "REVISION"):
            expecting = True
            continue
        if expecting:
            expecting = False
            if token.type == "QUOTED_STRING":
                stamps.append(token.value.strip('"').strip().rstrip("Z"))

    usable = [s for s in stamps if s.isdigit() and len(s) >= 6]
    if not usable:
        return "--"

    newest = max(usable)
    if len(newest) < 12:
        century = "19" if int(newest[:2]) >= 70 else "20"
        newest = century + newest

    return f"{newest[:4]}-{newest[4:6]}-{newest[6:8]}"


def as_utf8(data: bytes) -> bytes:
    """Re-encode a publisher's text as UTF-8 if it is not already.

    Vendors ship MIBs with Windows-1252 smart quotes in DESCRIPTIONs often
    enough to matter. Storing those bytes as they arrive puts a file in
    ``src/`` that ``read_text()`` cannot open. Transcoding is
    deterministic, so ``--check`` still compares byte for byte afterwards.
    """
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("cp1252").encode("utf-8")

    return data


def normalize_eol(data: bytes) -> bytes:
    """Convert CRLF and lone CR line endings to LF.

    A vendor serving the same module over time from a Windows build tree
    and a Unix one would otherwise read as a wholesale rewrite. Only the
    line endings move; nothing else in the text is touched.
    """
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


#: Archives already pulled during this run. A vendor that ships its whole
#: MIB set in one zip must be downloaded once, not once per module.
_archives: dict[str, zipfile.ZipFile] = {}


def _archive(url: str) -> zipfile.ZipFile:
    """The zip at *url*, downloaded at most once per run."""
    if url not in _archives:
        _archives[url] = zipfile.ZipFile(io.BytesIO(download(url)))

    return _archives[url]


def module_of(path: str) -> str:
    """The module name a checked-in file holds, from its path.

    This repository names each file after the module inside it, with no
    extension. ``mibdump`` resolves imports by that filename, so the two
    cannot drift apart.
    """
    return path.rsplit("/", 1)[-1]


def fetch(path: str, entry: dict[str, Any], publisher: dict[str, Any]) -> bytes:
    """The publisher's own text for the module checked in at *path*.

    The patch, if the module has one, is *not* applied here -- callers
    that want the publisher's baseline and callers that want what should
    be on disk both go through this and differ in what they do next.

    Raises:
        Unreachable: the publisher could not be reached.
        NotAModule: the publisher served something that is not this MIB.
    """
    module = module_of(path)
    kind = publisher["kind"]

    if kind == "file":
        url = publisher["url"].format(module=module, **entry.get("vars", {}))
        data = download(url)
    elif kind == "archive":
        member = publisher["member"].format(module=module, **entry.get("vars", {}))
        try:
            data = _archive(publisher["url"]).read(member)
        except KeyError as exc:
            raise NotAModule(f"{member} is not in the archive") from exc
    else:
        raise SystemExit(f"{path}: unknown publisher kind {kind!r}")

    return require_module(normalize_eol(as_utf8(data)), module)


HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def apply_patch(text: bytes, patch: str, label: str) -> bytes:
    """Apply a unified diff, refusing anything whose context has moved.

    Deliberately strict and dependency-free, the way pysmi applies the
    patches for its bundled MIBs. A patch that no longer matches the text
    it was cut against means the publisher has revised the module under
    it -- which is the whole thing the monthly sweep exists to notice, so
    fuzzing past it would defeat the point.

    Raises:
        ValueError: the patch does not apply to *text*.
    """
    lines = text.decode("utf-8", "replace").split("\n")
    out: list[str] = []
    cursor = 0

    for chunk in patch.split("\n"):
        if chunk.startswith(("--- ", "+++ ")):
            continue

        header = HUNK.match(chunk)
        if header:
            start = int(header.group(1)) - 1
            if start < cursor:
                raise ValueError(f"{label}: overlapping hunks in its patch")
            out.extend(lines[cursor:start])
            cursor = start
            continue

        if not chunk:
            continue

        mark, body = chunk[0], chunk[1:]

        if mark == "+":
            out.append(body)
        elif mark in " -":
            if cursor >= len(lines) or lines[cursor] != body:
                if cursor < len(lines):
                    found = lines[cursor]
                else:
                    found = "<end of file>"
                raise ValueError(
                    f"{label}: its patch no longer applies -- line "
                    f"{cursor + 1} reads {found!r}, the patch expects "
                    f"{body!r}"
                )
            if mark == " ":
                out.append(body)
            cursor += 1
        elif mark == "\\":
            continue
        else:
            raise ValueError(f"{label}: unreadable patch line: {chunk!r}")

    out.extend(lines[cursor:])

    return "\n".join(out).encode()


def make_patch(baseline: bytes, wanted: bytes, module: str) -> str:
    """A unified diff turning the publisher's text into ours.

    Written with no context lines beyond the three a reviewer needs, and
    against the module name rather than a path, so a patch reads as a
    statement about the module and not about where a checkout put it.
    """
    diff = difflib.unified_diff(
        baseline.decode("utf-8", "replace").split("\n"),
        wanted.decode("utf-8", "replace").split("\n"),
        fromfile=f"a/{module}",
        tofile=f"b/{module}",
        lineterm="",
    )

    return "\n".join(diff) + "\n"


def wanted_text(path: str, entry: dict[str, Any], publisher: dict[str, Any]) -> bytes:
    """What should be checked in at *path*: the publisher's text, patched."""
    data = fetch(path, entry, publisher)

    if "patch" in entry:
        patch = (PATCHES / entry["patch"]).read_text()
        data = apply_patch(data, patch, module_of(path))

    return data


def _git(*args: str) -> str:
    """Run git in the repository and return its stdout."""
    result = subprocess.run(
        ("git", *args),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    return result.stdout


def import_commits(path: str) -> set[str]:
    """The commits that brought *path* into this repository.

    Everything a file arrived with is attributable only to these, which
    tells us nothing: the bulk imports carried whatever the snmplabs and
    librenms collections had already done to the text. So this is the
    boundary between an edit we can explain and one we cannot.

    Both spellings are needed. Without ``--follow`` git names the commit
    that created the file at the path it sits at now; with it, git
    follows the renames back and names the one that first brought the
    text in under some earlier path. A file that has been refiled -- and
    plenty here have, as vendor directories were split apart -- has two
    such commits, and crediting a later edit to either of them would read
    an import as a repair.
    """
    commits = set()

    for follow in ((), ("--follow",)):
        log = _git("log", "--diff-filter=AR", *follow, "--format=%H", "--", path)
        commits.update(log.split())

    return commits


def changed_ranges(baseline: bytes, ours: bytes) -> tuple[list[tuple[int, int]], int]:
    """How *ours* differs from *baseline*, in terms git can be asked about.

    Returns:
        The 1-based line ranges of *ours* holding text the publisher does
        not have, and the number of hunks that only *remove* publisher
        text.

    The split matters. A line we wrote is a line git can name a commit
    for. A line we deleted leaves nothing behind to blame -- it exists
    only in the publisher's copy -- so counting it as unattributable
    would make every deletion look like inherited, unexplainable
    patching. It is reported as its own number instead.
    """
    matcher = difflib.SequenceMatcher(
        None,
        baseline.decode("utf-8", "replace").split("\n"),
        ours.decode("utf-8", "replace").split("\n"),
        autojunk=False,
    )
    ranges = []
    deletions = 0

    for tag, _, _, start, stop in matcher.get_opcodes():
        if tag == "equal":
            continue
        if start == stop:
            deletions += 1
        else:
            ranges.append((start + 1, stop))

    return ranges, deletions


def attribute(path: str, ranges: Iterable[tuple[int, int]]) -> tuple[list[str], bool]:
    """Name the commits of ours that produced the given lines of *path*.

    Returns:
        The commit subjects that last wrote those lines, newest first,
        and whether any range was last written by the import itself --
        that second value being the silent, unattributable patching this
        repository inherited and cannot recover.

    Only the *newest* commit to touch a range counts. Every line in a
    file carries its import somewhere in its history, since that is
    where the file began, so asking whether the import appears at all
    would mark everything inherited. Asking whether anything came after
    it is what separates a repair we made from text we received.
    """
    imported = import_commits(path)
    subjects: dict[str, None] = {}
    inherited = False

    for start, stop in ranges:
        log = _git(
            "log",
            f"-L{start},{stop}:{path}",
            "--format=%x00%H %ad %s",
            "--date=short",
        )
        touching = [
            line[1:]
            for line in log.split("\n")
            if line.startswith("\x00") and line[1:].strip()
        ]

        if not touching:
            inherited = True
            continue

        commit, rest = touching[0].split(" ", 1)

        if commit in imported:
            inherited = True
        else:
            subjects[rest] = None

    return list(subjects), inherited

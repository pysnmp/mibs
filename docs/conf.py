"""Sphinx configuration for the pysnmp MIB distribution documentation.

This builds https://pysnmp.github.io/mibs/, which is published onto the same
gh-pages tree as the corpus it describes -- so the documentation for a channel
and the channel itself are deployed by the same run and cannot drift apart by a
release. It lands at the site root, which until now answered 404: every path
the corpus serves is a directory or a CSV, and none of them collide with a
Sphinx page.

The source directory is ``docs/`` rather than ``docs/source/`` because two of
these pages predate the site and are linked by path from the README and from
the contract scripts. Moving them to gain one directory level would break
those links for no reader's benefit.
"""

import pathlib
import sys

# -- Project information -----------------------------------------------------

project = "pysnmp MIB distribution"
author = "The pysnmp maintainers"
copyright = "2019-2026, the pysnmp maintainers"

# The corpus is rebuilt from the same sources on every run and published
# continuously; what the site serves is whatever main last built. There is no
# version of the documentation distinct from that, so |version| and |release|
# are left empty and the theme is configured not to show them.
version = ""
release = ""

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.extlinks",
]

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"
language = "en"
exclude_patterns = [
    "_build",
    # The uv project that builds this site lives beside its sources; see the
    # module docstring for why the two share a directory.
    "pyproject.toml",
    "uv.lock",
    ".venv",
]
pygments_style = "sphinx"

# The same roles the organization site and the three library sites define, so
# a cross-reference is written the same way wherever it appears.
extlinks = {
    "repo": ("https://github.com/pysnmp/%s", "pysnmp/%s"),
    "docs": ("https://pysnmp.github.io/%s/", "%s documentation"),
}
# Deep links into a sibling site (a single page, not its root) cannot be
# written as one of the roles above, and this repository has several. Left off
# so a legitimate deep link is not reported as a missed extlink.
extlinks_detect_hardcoded_links = False

# GitHub issue references. The prose here cites them constantly -- a
# deprecation window, a migration, the issue that removed a second
# implementation -- and a bare number is not a link.
extlinks["issue"] = ("https://github.com/pysnmp/mibs/issues/%s", "#%s")

myst_heading_anchors = 3

# Substitution, so a page writes {{ modules }} where a count belongs and this
# file supplies it. See the figures block below.
myst_enable_extensions = ["substitution"]

# -- The corpus's own figures ------------------------------------------------
#
# Every count this distribution publishes changes when a MIB is added. Written
# into prose by hand, each one is wrong at the next contribution and is a diff
# to review on every one after that -- and they were: the pages said 5,510
# modules for long enough that the corpus passed 7,000.
#
# So no page states a count. A page names a figure, {{ modules }} or
# |modules|, and scripts/corpus_figures.py supplies it from the build report
# the corpus build wrote and from the committed artifacts -- index-frozen.csv,
# the PEN snapshot, the missing-import baseline, src/ itself. CI builds the
# corpus in this same job before it builds these pages, so the published
# figure is the one that build measured.
#
# A checkout with no build still renders: a figure only the build knows falls
# back to a phrase naming the scale rather than to a wrong number. Run
# `make corpus` first, or point MIBS_CORPUS_REPORT at a report.json, to see
# the numbers locally.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import corpus_figures

myst_substitutions = corpus_figures.figures()

# The same figures for the reStructuredText pages, which do not read
# myst_substitutions. Written as a prolog rather than per page so a figure is
# defined once however many pages name it.
rst_prolog = "\n".join(
    f".. |{name}| replace:: {value}"
    for name, value in sorted(myst_substitutions.items())
)

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

# The theme the organization site and the three library sites use, so moving
# between the five is moving within one site.
html_theme_options = {
    "light_logo": "logo.svg",
    "dark_logo": "logo.svg",
    "source_repository": "https://github.com/pysnmp/mibs/",
    "source_branch": "main",
    "source_directory": "docs/",
}

html_title = "pysnmp MIB distribution"
html_short_title = "MIB distribution"
html_favicon = ".static/favicon.ico"
html_static_path = [".static"]
html_show_sourcelink = False
html_copy_source = False
html_domain_indices = False
html_use_index = False

# -- Options for the link checker --------------------------------------------

linkcheck_anchors = False
linkcheck_timeout = 30
linkcheck_retries = 2
linkcheck_ignore = [
    # Every module under here is generated and the tree carries no HTML index,
    # so a link to the directory is a 404 by design -- the paths below it are
    # what resolve. The `asn1/@mib@` form is a pysmi source template rather
    # than a URL at all.
    r"https://pysnmp\.github\.io/mibs/asn1/?$",
    r"https://pysnmp\.github\.io/mibs/json/?$",
    r".*@mib@.*",
]

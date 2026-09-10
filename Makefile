.DEFAULT_GOAL := help
PY ?= uv run
MIBCORPUS ?= $(PY) mibcorpus

# The two corpora, and the manifest that declares each one's source set.
#
# They differ in one line: corpus-compact.json marks the standard namespace
# "publish": false, so pysmi's bundled modules resolve what the vendor modules
# import without being carried. Everything else -- the source set, the
# precedence between two namespaces holding one module name, the OID ranking --
# is the same, so the compact corpus is a subset of the full one rather than a
# second rendering of it.
CORPUS_MANIFEST ?= corpus.json
CORPUS_OUT ?= output
COMPACT_MANIFEST ?= corpus-compact.json
COMPACT_OUT ?= output-compact

# The OID index is a projection of the jsondoc tree, so the compact build has
# to produce jsondoc even though the compact corpus does not carry it. --emit
# takes a path, so it is written here, outside the corpus, and removed.
COMPACT_SCRATCH ?= build/compact-jsondoc

# The corpus database, which is neither of the two corpora above: it is the
# same source set again, laid out for lookup instead of for serving.
DB_OUT ?= output-db
DB_SCRATCH ?= build/db-jsondoc

# What the database says it is. Neither is invented at build time: a version
# read from a clock or a checkout would make two builds of one source tree
# differ, and core.db is written to be reproducible.
#
# The default is the working tree's version, which is right for a local build.
# CI overrides it with the version semantic-release is about to publish --
# because semantic-release bumps pyproject.toml *after* the artifacts are
# built, so a database stamped from the tree names the previous release. That
# is how v2.1.0 shipped a core.db saying 2.0.2.
CORPUS_ID ?= pysnmp/mibs
CORPUS_VERSION ?= $(shell sed -n 's/^version = "\(.*\)"/\1/p' pyproject.toml)

.PHONY: all corpus corpus-compact corpus-db render help

corpus:  ## Build the published corpus into output/
	@# Everything the site serves, in one deterministic pass: the ASN.1 as
	@# published, jsondoc, both OID indexes and the standard module list.
	@# index.csv replays index-frozen.csv, so a consumer keying on the module
	@# an OID resolves to keeps the answer it already has; corrections land
	@# in index-v2.csv.
	@#
	@# The artifacts are named rather than left to the default layout, and
	@# what the naming leaves out is the point: notexts and texts are pysnmp
	@# modules, and a pysnmp module is Python that MibBuilder exec()s -- so
	@# publishing them over HTTP offers every consumer a way to run code
	@# fetched from this site. Nothing needs them: pysnmp resolves from local
	@# directories by default, splunk-connect-for-snmp binds asn1/@mib@ and
	@# compiles with pysmi, and json carries the same facts as data. Pull the
	@# MIB and compile it; that is the safe shape and it is what consumers
	@# already do.
	$(MIBCORPUS) --manifest=$(CORPUS_MANIFEST) \
	  --output-directory=$(CORPUS_OUT) \
	  --emit=asn1 --emit=json \
	  --emit=index --emit=index-v2 --emit=standard --emit=report \
	  --frozen-index=index-frozen.csv
	touch $(CORPUS_OUT)/.nojekyll

corpus-compact:  ## Build the compact corpus into output-compact/
	@# What a pysnmp runtime needs to poll and to translate a trap OID, and
	@# nothing else: the ASN.1 to compile, and an OID index to decide which
	@# module answers for an OID. This image is mounted by the runtime rather
	@# than served to the world, so it carries a dependency rather than a
	@# mirror.
	@#
	@# So no standard.txt and no legacy index.csv -- both are compatibility
	@# surfaces of the published corpus, and a runtime with no legacy answers
	@# to preserve wants index-v2. No json either: it is data for other
	@# tooling, not something pysnmp reads. And no pysnmp modules, which is
	@# the point -- they are Python that MibBuilder exec()s, and a runtime
	@# that compiles what it pulls has no use for a tree of them.
	@#
	@# For a runtime that already has the standard modules: pysmi bundles 210
	@# and its wheel ships their compiled form, so restating them costs size
	@# and says nothing new.
	rm -rf $(COMPACT_SCRATCH)
	$(MIBCORPUS) --manifest=$(COMPACT_MANIFEST) \
	  --output-directory=$(COMPACT_OUT) \
	  --emit=asn1 --emit=json:$(COMPACT_SCRATCH) \
	  --emit=index-v2 --emit=report
	@# The jsondoc is scratch because the compact corpus does not carry it --
	@# but it is also the only rendering of how these modules *compiled*, and
	@# tests/corpus-agreement.py compares that against the published corpus.
	@# CI sets KEEP_COMPACT_JSONDOC to fingerprint it before it goes.
	$(if $(KEEP_COMPACT_JSONDOC),,rm -rf $(COMPACT_SCRATCH))

corpus-db:  ## Build the corpus database into output-db/
	@# core.db: every node the corpus defines, keyed for lookup by OID and by
	@# name and ordered so a GETNEXT walk is a range query. pysnmp reads it
	@# with stdlib sqlite3 and no pysmi import; the format is specified in
	@# pysmi's corpus-schema document.
	@#
	@# Built from corpus.json, the *full* source set, not from the compact
	@# manifest. The compact corpus leaves the standard modules out because a
	@# runtime that has pysmi already holds them as Python -- but a corpus is
	@# consulted by OID, and an OID index missing 1.3.6.1.2.1 cannot resolve
	@# ifDescr for anyone. There is one corpus; vendor is a column in it, not
	@# a partition of it.
	@#
	@# No texts. DESCRIPTION and REFERENCE are about a third of a module's
	@# bytes, pysnmp discards them under the default loadTexts=False, and the
	@# published json/ tree already serves the one consumer that wants them --
	@# a MIB browser. A second database for prose would be the largest thing
	@# this repository publishes and would duplicate a channel that works.
	@#
	@# The database is a projection of the jsondoc tree, exactly as the two
	@# indexes are, so the build has to emit json. It goes to a scratch path
	@# outside the corpus and is removed: what this target publishes is one
	@# file.
	rm -rf $(DB_SCRATCH)
	@test -n "$(CORPUS_VERSION)" || { echo "CORPUS_VERSION is empty"; exit 1; }
	$(MIBCORPUS) --manifest=$(CORPUS_MANIFEST) \
	  --output-directory=$(DB_OUT) \
	  --emit=core-db --emit=json:$(DB_SCRATCH) \
	  --emit=report \
	  --corpus-id=$(CORPUS_ID) --corpus-version=$(CORPUS_VERSION)
	rm -rf $(DB_SCRATCH)

render:  ## Re-render the chart into rendered/manifests
	./render_manifests.sh

help:  ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f1- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

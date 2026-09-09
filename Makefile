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

.PHONY: all corpus corpus-compact render help

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
	$(MIBCORPUS) --manifest=$(COMPACT_MANIFEST) \
	  --output-directory=$(COMPACT_OUT) \
	  --emit=asn1 --emit=index-v2 --emit=report

render:  ## Re-render the chart into rendered/manifests
	./render_manifests.sh

help:  ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f1- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

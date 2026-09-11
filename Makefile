.DEFAULT_GOAL := help
PY ?= uv run
MIBCORPUS ?= $(PY) mibcorpus

# Each corpus is a manifest: it names its own source set, the artifacts it
# carries and what must be true of the result. What is left here is what a
# manifest cannot declare -- see docs/corpora.md for why each corpus is shaped
# the way it is.
CORPUS_ID ?= pysnmp/mibs
CORPUS_VERSION ?= $(shell sed -n 's/^version = "\(.*\)"/\1/p' pyproject.toml)

# The IANA registries the arc names come from, committed rather than fetched:
# a build with the network unplugged has to produce the same corpus as one
# without, and the enterprise registry changes daily. See
# scripts/update_registries.py and docs/registries.md.
OID_REGISTRIES ?= --oid-registry=registries/smi-numbers.xml \
	  --oid-registry=registries/pen-snapshot.csv

.PHONY: corpus corpus-compact corpus-db render help

corpus:  ## Build the published corpus into output/
	@# --frozen-index is the reason this target exists rather than a
	@# documented command line: a build that forgets it silently produces an
	@# index.csv that disagrees with the published one, which is the exact
	@# failure index-frozen.csv is kept to prevent.
	$(MIBCORPUS) --manifest=corpus.json \
	  --output-directory=output \
	  --frozen-index=index-frozen.csv \
	  $(OID_REGISTRIES)
	touch output/.nojekyll

corpus-compact:  ## Build the compact corpus into output-compact/
	$(MIBCORPUS) --manifest=corpus-compact.json \
	  --output-directory=output-compact

corpus-db:  ## Build the corpus database into output-db/
	@# CI overrides CORPUS_VERSION with the version semantic-release is about
	@# to publish; the default is right for a local build. See docs/corpora.md.
	@test -n "$(CORPUS_VERSION)" || { echo "CORPUS_VERSION is empty"; exit 1; }
	$(MIBCORPUS) --manifest=corpus-db.json \
	  --output-directory=output-db \
	  --corpus-id=$(CORPUS_ID) --corpus-version=$(CORPUS_VERSION)

render:  ## Re-render the chart into rendered/manifests
	./render_manifests.sh

help:  ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f1- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

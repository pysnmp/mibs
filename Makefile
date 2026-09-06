.DEFAULT_GOAL := help
PY ?= uv run
.PHONY: all vendor bundled-asn1
#RFC=$(notdir $(wildcard mibs/*))
RFC=$(wildcard src/standard/*)

# fetch:  ## Download all mibs from the source
# 	@# Wget recursive
# 	wget --recursive --reject-regex 'index.html*' \
# 	  --no-parent --no-host-directories http://mibs.snmplabs.com/asn1/
# 	rm -rf asn1/index.html*
dirs:
	mkdir -p output/asn1/ || true
	mkdir -p output/texts/ || true
	mkdir -p output/notexts/ || true
	mkdir -p output/json/ || true
	mkdir -p log || true

bundled-asn1: dirs  ## Stage pysmi's bundled ASN.1 sources into the published asn1 tree
	@bundle=$$($(PY) python -c 'import pysmi.mibs.asn1 as m; print(m.__path__[0])'); \
	  test -n "$$bundle" -a -d "$$bundle" || { echo "cannot locate pysmi bundled asn1"; exit 1; }; \
	  find "$$bundle" -maxdepth 1 -type f ! -name '*.py' ! -name '*.pyc' -exec cp -f {} output/asn1/ \;

render:
	rm -rf rendered/manifests/*
	helm template --namespace default --output-dir rendered/manifests/default default charts/mibserver
	./render_manifests.sh

standard: bundled-asn1 $(RFC)
	@# Compile mibs

	{ find src/standard -type f; find output/asn1 -maxdepth 1 -type f; } | sed 's|^.*\/||g' | grep -v '^\.' | grep -v '^RFC' | grep -v '^SNMPv2' | sort | uniq >output/standard.txt
	./scripts/vendorsingle.sh output/asn1
	./scripts/vendor.sh standard	

vendor: bundled-asn1 $(RFC)
	./scripts/vendor.sh vendor

localmibs:
	find src/vendor -type d -maxdepth 1 -mindepth 1   | sort >list.tmp
	while read line; do ./scripts/localmibs.sh "$$line"; done < list.tmp

index: standard vendor  ##generate index
	touch output/.nojekyll
	$(PY) python index.py

index-local-mibs: bundled-asn1 $(RFC) localmibs
	touch output/.nojekyll
	$(PY) python index.py

compile-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD mibs/asn1/); do \
		echo "## Compiling $$f"; \
		$(PY) mibdump \
			--no-python-compile \
			--mib-source=file://$$(pwd)/src/standardasn1 \
			--destination-directory=./pysnmp \
			$$f; \
	done

compile-with-texts:  ## Compile With Texts all MIBs into .py files
	@for f in $$(ls mibs/asn1); do \
	  echo "## Compiling $$f with texts"; \
	  $(PY) mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/src/standardasn1 \
	    --destination-directory=./pysnmp-with-texts \
	    $$f; \
	done

compile-with-texts-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD mibs/asn1/); do \
	  echo "## Compiling $$f with texts"; \
	  $(PY) mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/src/standardasn1 \
	    --destination-directory=./pysnmp-with-texts \
	    $$f; \
	done

compile-json:  ## Compile With Texts all MIBs into .py files
	@for f in $$(ls output/asn1); do \
	  echo "## Compiling $$f with texts"; \
	  $(PY) mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/src/standardasn1 \
	    --destination-format=json \
	    --destination-directory=./mibs/json \
	    $$f; \
	done

compile-json-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD mibs/asn1/); do \
	  echo "## Compiling $$f with texts"; \
	  $(PY) mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/src/standardasn1 \
	    --destination-format=json \
	    --destination-directory=./mibs/json \
	    $$f; \
	done

help:  ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f1- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

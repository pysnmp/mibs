.DEFAULT_GOAL := help
.PHONY: all vendor
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

render:
	rm -rf rendered/manifests/*
	helm template --namespace default --output-dir rendered/manifests/default default charts/mibserver
	./render_manifests.sh

standard: #dirs $(RFC)
	@# Compile mibs

	find src/standard -type f | sed 's|^.*\/||g' | grep -v '^\.' | grep -v '^RFC' | grep -v '^SNMPv2' | sort | uniq >output/standard.txt
	./scripts/vendor.sh standard	

vendor: dirs $(RFC)
	./scripts/vendor.sh vendor

localmibs:
	find src/vendor -type d -maxdepth 1 -mindepth 1   | sort >list.tmp
	while read line; do ./scripts/localmibs.sh "$$line"; done < list.tmp

index: vendor standard  ##generate index
	touch output/.nojekyll
	poetry run python index.py

index-local-mibs: dirs $(RFC) localmibs
	touch output/.nojekyll
	poetry run python index.py

compile-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD mibs/asn1/); do \
		echo "## Compiling $$f"; \
		poetry run mibdump \
			--no-python-compile \
			--mib-source=file://$$(pwd)/src/standardasn1 \
			--destination-directory=./pysnmp \
			$$f; \
	done

compile-with-texts:  ## Compile With Texts all MIBs into .py files
	@for f in $$(ls mibs/asn1); do \
	  echo "## Compiling $$f with texts"; \
	  poetry run mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/src/standardasn1 \
	    --destination-directory=./pysnmp-with-texts \
	    $$f; \
	done

compile-with-texts-changed:  ## Compile With Texts all MIBs into .py files
	@for f in $$(git diff --name-only --diff-filter=AM HEAD mibs/asn1/); do \
	  echo "## Compiling $$f with texts"; \
	  poetry run mibdump \
	    --generate-mib-texts \
	    --no-python-compile \
	    --mib-source=file://$$(pwd)/src/standardasn1 \
	    --destination-directory=./pysnmp-with-texts \
	    $$f; \
	done

compile-json:  ## Compile With Texts all MIBs into .py files
	@for f in $$(ls output/asn1); do \
	  echo "## Compiling $$f with texts"; \
	  poetry run mibdump \
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
	  poetry run mibdump \
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

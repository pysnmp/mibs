#!/usr/bin/env bash
echo $1
v=$(basename $1)
mib=$(find $1 -type f ! -name '.*'  | sed 's|$1/||g')
d=$(dirname $1)

# A vendor directory may name other source directories it depends on, one
# repository-relative path per line, in a .mib-sources file. Used where an OEM
# SMI anchor is shared by two vendors and cannot live in either one.
extra=
if [ -f "$1/.mib-sources" ]; then
        while IFS= read -r src; do
                case "$src" in ''|'#'*) continue ;; esac
                extra="$extra --mib-source=file://$(pwd)/$src/"
        done <"$1/.mib-sources"
fi

${MIBDUMP:-uv run mibdump} \
        --cache-directory=.pycache \
        --mib-source=file://$1/ $extra --mib-source=file://$(pwd)/output/asn1 --mib-source=https://pysnmp.github.io:443/mibs/asn1/@mib@ \
        --destination-directory=./output/notexts $mib >log/$v-nt.log 2>log/$v-nt.err

${MIBDUMP:-uv run mibdump} \
        --cache-directory=.pycache \
        --mib-source=file://$1/ $extra --mib-source=file://$(pwd)/output/asn1 --mib-source=https://pysnmp.github.io:443/mibs/asn1/@mib@ \
        --destination-directory=./output/texts \
        --generate-mib-texts --keep-texts-layout $mib >log/$v-t.log 2>log/$v-t.err

${MIBDUMP:-uv run mibdump} \
	--ignore-errors \
 	--cache-directory=.pycache \
        --mib-source=file://$1/ $extra --mib-source=file://$(pwd)/output/asn1 --mib-source=https://pysnmp.github.io:443/mibs/asn1/@mib@ \
	--destination-directory=./output/json --destination-format=json \
	 $mib >log/$v-j.log 2>log/$v-j.err


# Skip when compiling the staged bundle itself: source and target are the same tree.
[ "$(cd "$1" && pwd)" = "$(pwd)/output/asn1" ] || cp -f $1/* output/asn1
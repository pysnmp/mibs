#!/usr/bin/env bash
echo $1
v=$(basename $1)
mib=$(find $1 -type f  | sed 's|$1/||g')
d=$(dirname $1)
MIB_SOURCE_URL=${MIB_SOURCE_URL:-https://splunk.github.io/mibs/asn1/@mib@}
poetry run mibdump \
        --cache-directory=.pycache \
        --mib-source=file://$1/ --mib-source=file://$(pwd)/output/asn1 --mib-source="$MIB_SOURCE_URL" \
        --destination-directory=./output/notexts $mib >log/$v-nt.log 2>log/$v-nt.err

poetry run mibdump \
        --cache-directory=.pycache \
        --mib-source=file://$1/ --mib-source=file://$(pwd)/output/asn1 --mib-source="$MIB_SOURCE_URL" \
        --destination-directory=./output/texts \
        --generate-mib-texts --keep-texts-layout $mib >log/$v-t.log 2>log/$v-t.err

poetry run mibdump \
	--ignore-errors \
 	--cache-directory=.pycache \
        --mib-source=file://$1/ --mib-source=file://$(pwd)/output/asn1 --mib-source="$MIB_SOURCE_URL" \
	--destination-directory=./output/json --destination-format=json \
	 $mib >log/$v-j.log 2>log/$v-j.err


find "$1" -type f -exec sh -c 'cp -f "$@" output/asn1/' sh {} +

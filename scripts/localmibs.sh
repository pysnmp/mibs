#!/usr/bin/env bash
echo $1
v=$(basename $1)
mib=$(find $1 -type f  | sed 's|$1/||g')
d=$(dirname $1)

echo "Compiling $mib ..."
poetry run mibdump \
        --cache-directory=.pycache \
        --mib-source=file://$1/ --mib-source=file://$(pwd)/output/asn1 --mib-source=file:///usr/share/nginx/html/asn1
         --mib-source=https://pysnmp.github.io:443/mibs/asn1/@mib@ \
        --destination-directory=./output/notexts $mib

poetry run mibdump \
        --cache-directory=.pycache \
        --mib-source=file://$1/ --mib-source=file://$(pwd)/output/asn1 --mib-source=file:///usr/share/nginx/html/asn1
         --mib-source=https://pysnmp.github.io:443/mibs/asn1/@mib@ \
        --destination-directory=./output/texts \
        --generate-mib-texts --keep-texts-layout $mib

poetry run mibdump \
	--ignore-errors \
 	--cache-directory=.pycache \
        --mib-source=file://$1/ --mib-source=file://$(pwd)/output/asn1 --mib-source=file:///usr/share/nginx/html/asn1
         --mib-source=https://pysnmp.github.io:443/mibs/asn1/@mib@ \
	--destination-directory=./output/json --destination-format=json \
	 $mib

cp -f $1/* output/asn1
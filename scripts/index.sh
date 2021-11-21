#!/usr/bin/env bash
command_exists() {
    # check if command exists and fail otherwise
    command -v "$1" >/dev/null 2>&1
    if [[ $? -ne 0 ]]; then
        echo "I require $1 but it's not installed. Abort."
        exit 1
    fi
}
command_exists "grep"
command_exists "sed"

echo from inside index.sh
grep -Po 'ModuleIdentity\(\(((?:\d(?:, )?)*)\)\)' output/notexts/* \
	| sed 's|.*/notexts/||' \
	| sed 's|, |.|g' \
	| sed 's|.py:ModuleIdentity((|,|' \
	| sed 's|))||' >list.csv

while IFS=, read -r one two; do 
    d=$(echo $two | sed 's|\.|/|g')
    mkdir -p output/index/$d
    echo $one>>output/index/$d/mib.txt
    echo $d, $one
    echo $one,$two>>output/index.csv
done <list.csv

rm -f output/texts/SNMPv2-MIB*
rm -f output/texts/INET-ADDRESS-MIB*
rm -f output/texts/PYSNMP-USM-MIB*
rm -f output/texts/RFC-1212*
rm -f output/texts/RFC-1215*
rm -f output/texts/RFC1065-SMI*
rm -f output/texts/RFC1155-SMI*
rm -f output/texts/RFC1158-MIB*
rm -f output/texts/RFC1213-MIB*
rm -f output/texts/SNMP-FRAMEWORK-MIB*
rm -f output/texts/SNMP-TARGET-MIB*
rm -f output/texts/SNMPv2-CONF*
rm -f output/texts/SNMPv2-SMI*
rm -f output/texts/SNMPv2-TC*
rm -f output/texts/SNMPv2-TM*
rm -f output/texts/TRANSPORT-ADDRESS-MIB*

rm -f output/notexts/SNMPv2-MIB*
rm -f output/notexts/INET-ADDRESS-MIB*
rm -f output/notexts/PYSNMP-USM-MIB*
rm -f output/notexts/RFC-1212*
rm -f output/notexts/RFC-1215*
rm -f output/notexts/RFC1065-SMI*
rm -f output/notexts/RFC1155-SMI*
rm -f output/notexts/RFC1158-MIB*
rm -f output/notexts/RFC1213-MIB*
rm -f output/notexts/SNMP-FRAMEWORK-MIB*
rm -f output/notexts/SNMP-TARGET-MIB*
rm -f output/notexts/SNMPv2-CONF*
rm -f output/notexts/SNMPv2-SMI*
rm -f output/notexts/SNMPv2-TC*
rm -f output/notexts/SNMPv2-TM*
rm -f output/notexts/TRANSPORT-ADDRESS-MIB*

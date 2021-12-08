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

grep -Po ' enterprises +(\d+)' asn1/* | sort | uniq | sed 's|asn1\/||g' | sed 's|: enterprises |,|g' >output/enterprises.csv
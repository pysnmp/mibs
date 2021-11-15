
grep -Eo 'ModuleIdentity\(\(((?:\d(?:, )?)*)\)\)' output/notexts/* \
	| sed 's|output/notexts/||' \
	| sed 's|, |.|g' \
	| sed 's|.py:ModuleIdentity((|,|' \
	| sed 's|))||' >output/index.csv
while IFS=, read -r one two; do 
    d=$(echo $two | sed 's|\.|/|g')
    mkdir -p output/index/$d
    echo $one>>output/index/$d/mib.txt
    echo $d, $one    
done <output/index.csv
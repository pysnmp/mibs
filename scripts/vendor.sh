
cust_func(){
    mib=$(basename $1)
    d=$(dirname $1)
    poetry run mibdump \
            --no-python-compile \
            --mib-source=file://$(pwd)/$d/ --mib-source=file://$(pwd)/output/asn1 \
            --destination-directory=./output/notexts $mib

    poetry run mibdump \
    --no-python-compile \
    --mib-source=file://$(pwd)/$d/ --mib-source=file://$(pwd)/output/asn1 \
    --destination-directory=./output/texts \
    --generate-mib-texts --keep-texts-layout $mib

    cp -f $1 output/asn1/
}


find src/vendor -type f >list.tmp
while IFS=, read -r mibpath; do 


    cust_func "$mibpath" &
done <list.tmp

echo waiting
wait
echo done
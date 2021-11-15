    
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
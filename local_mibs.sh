#!/bin/bash
if [ -n "$(ls -A /app/new_mibs/src/vendor 2>/dev/null)" ]
then
  cd /app/new_mibs
  mkdir -p output/asn1 output/texts output/notexts output/json log
  echo "**********************************"
  echo "Found local mibs. Compiling..."
  echo "**********************************"
  find src/vendor -type d -maxdepth 1 -mindepth 1 | sort >list.tmp
  while read -r line; do ./scripts/localmibs.sh "$line"; done <list.tmp
  touch output/.nojekyll
  python index.py
  echo "**********************************"
  echo "Successfully compiled MIBs are: "
  echo "**********************************"
  sed 's/,.*//g' /app/new_mibs/output/index.csv | uniq | sort
  # The convention here is to have no MIB extension (like .my or .mib) so we cut it off
  find /app/new_mibs/output/asn1 -type f -name '*.*' | while read f; do mv "$f" "${f%.*}"; done
  echo "**********************************"
  echo "Preparing new mibs to be served..."
  echo "**********************************"
  cp -a /app/new_mibs/output/asn1/. /usr/share/nginx/html/asn1/
  sort -u /app/new_mibs/output/index.csv /usr/share/nginx/html/index.csv > /usr/share/nginx/html/index_merged.csv
  mv /usr/share/nginx/html/index_merged.csv /usr/share/nginx/html/index.csv
else
  echo "No local mibs. Skipping..."
fi

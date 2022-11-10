#!/bin/bash
if [ -n "$(ls -A /tmp/new_mibs/src/vendor/new 2>/dev/null)" ]
then
  cd /tmp/new_mibs
  mkdir output
  source /tmp/.cache/pysnmp-mibs*/bin/activate
  echo "Found local mibs. Compiling..."
  make index
  # The convention here is to have no MIB extension (like .my or .mib) so we cut it off
  find /tmp/new_mibs/output/asn1 -type f -name '*.*' | while read f; do mv "$f" "${f%.*}"; done
  echo "Preparing new mibs to be served..."
  cp -a /tmp/new_mibs/output/asn1/. /usr/share/nginx/html/asn1/
  sort -u /tmp/new_mibs/output/index.csv /usr/share/nginx/html/index.csv > /usr/share/nginx/html/index_merged.csv
  mv /usr/share/nginx/html/index_merged.csv /usr/share/nginx/html/index.csv
else
  echo "No local mibs. Skipping..."
fi

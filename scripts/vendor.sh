#!/usr/bin/env bash
find src/vendor -type d | sort >list.tmp
parallel -a list.tmp ./scripts/vendorsingle.sh
echo done
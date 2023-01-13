#!/usr/bin/env bash
find src/$1 -type d -maxdepth 1 -mindepth 1   | sort >list.tmp
parallel -a list.tmp ./scripts/vendorsingle.sh
echo done
#!/usr/bin/env bash
find src/$2 -type d -maxdepth 1 -mindepth 1   | sort >list.tmp
parallel -a list.tmp ./scripts/$1
echo done
#!/usr/bin/env bash
set -euo pipefail
find src/$1 -type d -maxdepth 1 -mindepth 1   | sort >list.tmp
parallel --halt soon,fail=1 --jobs "${MIB_BUILD_JOBS:-2}" -a list.tmp ./scripts/vendorsingle.sh
echo done

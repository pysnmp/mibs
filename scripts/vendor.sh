#!/usr/bin/env bash
#!/usr/bin/env bash
find src/vendor -type f >list.tmp
parallel -a list.tmp ./scripts/vendorsingle.sh
echo done
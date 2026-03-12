#!/bin/bash
# Extract all sub-page links from downloaded TOC/index files
# and build a master download list

BASE_URL="https://big5.falundafa.org/chibig5"
OUT_DIR="D:/WORKCL/falundafa_books"

# Map of book index URL paths for resolving relative links
declare -A BOOK_BASES=(
  ["01_轉法輪"]="chibig5"
  ["02_法輪功"]="chibig5"
  ["03_法輪大法義解"]="chibig5"
  ["04_轉法輪法解"]="chibig5"
  ["05_轉法輪卷二"]="chibig5"
  ["07_大圓滿法"]="chibig5"
  ["09_精進要旨"]="chibig5"
  ["15_洪吟"]="chibig5"
  ["22_導航"]="chibig5"
  ["23_精進要旨二"]="chibig5"
  ["26_洪吟二"]="chibig5"
  ["28_各地講法一"]="chibig5"
  ["29_各地講法二"]="chibig5"
  ["30_各地講法三"]="chibig5"
  ["33_各地講法五"]="chibig5"
  ["34_各地講法六"]="chibig5"
  ["36_各地講法七"]="chibig5"
  ["39_洪吟三"]="chibig5"
  ["40_精進要旨三"]="chibig5"
  ["41_各地講法八"]="chibig5"
  ["42_各地講法九"]="chibig5"
  ["43_各地講法十"]="chibig5"
  ["44_各地講法十一"]="chibig5"
  ["46_洪吟五"]="chibig5/hy5/big5/web-20190618"
  ["47_各地講法十二"]="chibig5"
  ["48_各地講法十三"]="chibig5"
  ["50_各地講法十五"]="chibig5"
  ["51_洪吟六"]="chibig5/hy6"
)

TOTAL_SUBPAGES=0

for htmlfile in "$OUT_DIR"/*.html; do
  fname=$(basename "$htmlfile" .html)
  filesize=$(wc -c < "$htmlfile" | tr -d ' ')

  # Extract .htm links (excluding navigation links like ../chibig5.htm, up links, etc.)
  subpages=$(grep -oE 'href="[^"]*\.htm[l]?"' "$htmlfile" | sed 's/href="//;s/"//' | grep -v '^\.\.' | grep -v '^http' | sort -u)

  count=$(echo "$subpages" | grep -c '.' 2>/dev/null || echo 0)

  if [ "$count" -gt 0 ] && [ "$filesize" -lt 20000 ]; then
    echo "=== $fname (${filesize}B, ${count} sub-pages) ==="
    echo "$subpages"
    TOTAL_SUBPAGES=$((TOTAL_SUBPAGES + count))
    echo ""
  fi
done

echo "Total sub-pages to download: $TOTAL_SUBPAGES"

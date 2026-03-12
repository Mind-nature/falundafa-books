#!/bin/bash
# Download all sub-pages for books that have TOC/index pages
# Each book gets its own subdirectory

BASE="https://big5.falundafa.org/chibig5"
ROOT="D:/WORKCL/falundafa_books"
SUCCESS=0
FAIL=0
SKIP=0

download_page() {
  local url="$1"
  local outfile="$2"
  if [ -f "$outfile" ]; then
    SKIP=$((SKIP + 1))
    return 0
  fi
  if curl -s -f -L --connect-timeout 15 --max-time 60 -o "$outfile" "$url"; then
    SUCCESS=$((SUCCESS + 1))
    return 0
  else
    echo "  FAILED: $url"
    FAIL=$((FAIL + 1))
    return 1
  fi
}

download_book_subpages() {
  local book_name="$1"
  local base_url="$2"
  shift 2
  local pages=("$@")

  local dir="$ROOT/$book_name"
  mkdir -p "$dir"

  echo "=== $book_name (${#pages[@]} pages) ==="
  for page in "${pages[@]}"; do
    download_page "$base_url/$page" "$dir/$page"
  done
}

# 01 轉法輪
download_book_subpages "01_轉法輪" "$BASE" \
  zfl_01.htm zfl_1.htm zfl_2.htm zfl_3.htm zfl_4.htm \
  zfl_5.htm zfl_6.htm zfl_7.htm zfl_8.htm zfl_9.htm

# 02 法輪功
download_book_subpages "02_法輪功" "$BASE" \
  flg_1.htm flg_2.htm flg_3.htm flg_4.htm flg_5.htm

# 03 法輪大法義解
download_book_subpages "03_法輪大法義解" "$BASE" \
  yijie_1.htm yijie_2.htm yijie_3.htm yijie_4.htm yijie_5.htm

# 04 轉法輪法解
download_book_subpages "04_轉法輪法解" "$BASE" \
  fajie_1.htm fajie_2.htm fajie_3.htm fajie_4.htm fajie_5.htm fajie_6.htm

# 05 轉法輪卷二
pages05=()
for i in $(seq -w 1 27); do pages05+=("zfl2_$i.htm"); done
download_book_subpages "05_轉法輪卷二" "$BASE" "${pages05[@]}"

# 07 大圓滿法
download_book_subpages "07_大圓滿法" "$BASE" \
  dymf_1.htm dymf_2.htm dymf_3.htm dymf_4.htm

# 08 美國法會講法
download_book_subpages "08_美國法會講法" "$BASE" \
  mgjf_1.htm mgjf_2.htm mgjf_3.htm

# 09 精進要旨
pages09=()
for i in $(seq -w 1 80); do pages09+=("jjyz_$i.htm"); done
download_book_subpages "09_精進要旨" "$BASE" "${pages09[@]}"

# 22 導航
download_book_subpages "22_導航" "$BASE" \
  daohang_1.htm daohang_2.htm daohang_3.htm daohang_4.htm

# 23 精進要旨二
pages23=()
for i in $(seq -w 1 46); do pages23+=("jjyz2_$i.htm"); done
download_book_subpages "23_精進要旨二" "$BASE" "${pages23[@]}"

# 28 各地講法一
download_book_subpages "28_各地講法一" "$BASE" \
  jiangfa1_1.htm jiangfa1_2.htm jiangfa1_3.htm

# 29 各地講法二
download_book_subpages "29_各地講法二" "$BASE" \
  jiangfa2_1.htm jiangfa2_2.htm jiangfa2_3.htm jiangfa2_4.htm jiangfa2_5.htm

# 30 各地講法三
download_book_subpages "30_各地講法三" "$BASE" \
  jiangfa3_1.htm jiangfa3_2.htm

# 31 音樂與美術創作會講法
download_book_subpages "31_音樂與美術創作會講法" "$BASE" \
  yyms_1.htm yyms_2.htm

# 32 各地講法四
download_book_subpages "32_各地講法四" "$BASE" \
  jiangfa4_1.htm jiangfa4_2.htm jiangfa4_3.htm

# 33 各地講法五
download_book_subpages "33_各地講法五" "$BASE" \
  jiangfa5_1.htm jiangfa5_2.htm jiangfa5_3.htm

# 34 各地講法六
download_book_subpages "34_各地講法六" "$BASE" \
  jiangfa6_1.htm jiangfa6_2.htm jiangfa6_3.htm

# 36 各地講法七
download_book_subpages "36_各地講法七" "$BASE" \
  jiangfa7_1.htm jiangfa7_2.htm jiangfa7_3.htm jiangfa7_4.htm

# 39 洪吟三
pages39=()
for i in $(seq -f "%03g" 2 125); do pages39+=("hy3_$i.htm"); done
download_book_subpages "39_洪吟三" "$BASE" "${pages39[@]}"

# 40 精進要旨三
pages40=()
for i in $(seq -w 1 76); do pages40+=("jjyz3_$i.htm"); done
download_book_subpages "40_精進要旨三" "$BASE" "${pages40[@]}"

# 41 各地講法八
download_book_subpages "41_各地講法八" "$BASE" \
  jiangfa8_1.htm jiangfa8_2.htm jiangfa8_3.htm

# 42 各地講法九
download_book_subpages "42_各地講法九" "$BASE" \
  jiangfa9_1.htm jiangfa9_2.htm jiangfa9_3.htm

# 43 各地講法十
download_book_subpages "43_各地講法十" "$BASE" \
  jiangfa10_1.htm jiangfa10_2.htm jiangfa10_3.htm jiangfa10_4.htm

# 44 各地講法十一
download_book_subpages "44_各地講法十一" "$BASE" \
  jiangfa11_1.htm jiangfa11_2.htm jiangfa11_3.htm jiangfa11_4.htm

# 47 各地講法十二
download_book_subpages "47_各地講法十二" "$BASE" \
  jiangfa12_1.htm jiangfa12_2.htm jiangfa12_3.htm jiangfa12_4.htm

# 48 各地講法十三
download_book_subpages "48_各地講法十三" "$BASE" \
  jiangfa13_1.htm jiangfa13_2.htm jiangfa13_3.htm

# 49 各地講法十四
download_book_subpages "49_各地講法十四" "$BASE" \
  jiangfa14_1.htm jiangfa14_2.htm

# 50 各地講法十五
download_book_subpages "50_各地講法十五" "$BASE" \
  jiangfa15_1.htm jiangfa15_2.htm jiangfa15_3.htm jiangfa15_4.htm jiangfa15_5.htm

echo ""
echo "============================="
echo "Sub-page download complete!"
echo "Success: $SUCCESS"
echo "Failed:  $FAIL"
echo "Skipped: $SKIP"
echo "============================="

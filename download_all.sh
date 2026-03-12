#!/bin/bash
# Batch download all 51 Falun Dafa books (HTML)
BASE_URL="https://big5.falundafa.org"
OUT_DIR="D:/WORKCL/falundafa_books"

declare -a BOOKS=(
  "chibig5/zfl.htm|01_轉法輪"
  "chibig5/flg.htm|02_法輪功"
  "chibig5/yijie.htm|03_法輪大法義解"
  "chibig5/fajie.htm|04_轉法輪法解"
  "chibig5/zfl2.htm|05_轉法輪卷二"
  "chibig5/xini.htm|06_悉尼法會講法"
  "chibig5/dymf.htm|07_大圓滿法"
  "chibig5/mgjf.htm|08_美國法會講法"
  "chibig5/jjyz.htm|09_精進要旨"
  "chibig5/bmjf.htm|10_北美首屆法會講法"
  "chibig5/ozjf.htm|11_歐洲法會講法"
  "chibig5/changchun.htm|12_長春輔導員法會講法"
  "chibig5/singapore.htm|13_新加坡法會講法"
  "chibig5/swiss.htm|14_瑞士法會講法"
  "chibig5/hongyin.htm|15_洪吟"
  "chibig5/uswest.htm|16_美國西部法會講法"
  "chibig5/useast.htm|17_美國東部法會講法"
  "chibig5/australia.htm|18_澳大利亞法會講法"
  "chibig5/newzland.htm|19_新西蘭法會講法"
  "chibig5/canada.htm|20_加拿大法會講法"
  "chibig5/chicago.htm|21_美國中部法會講法"
  "chibig5/daohang.htm|22_導航"
  "chibig5/jjyz2.htm|23_精進要旨二"
  "chibig5/na2002.htm|24_北美巡迴講法"
  "chibig5/la2003.htm|25_二零零三年元宵節講法"
  "chibig5/hongyin2.htm|26_洪吟二"
  "chibig5/houston.htm|27_休斯頓法會講法"
  "chibig5/jiangfa1.htm|28_各地講法一"
  "chibig5/jiangfa2.htm|29_各地講法二"
  "chibig5/jiangfa3.htm|30_各地講法三"
  "chibig5/yyms.htm|31_音樂與美術創作會講法"
  "chibig5/jiangfa4.htm|32_各地講法四"
  "chibig5/jiangfa5.htm|33_各地講法五"
  "chibig5/jiangfa6.htm|34_各地講法六"
  "chibig5/ny2004.htm|35_二零零四年紐約國際法會講法"
  "chibig5/jiangfa7.htm|36_各地講法七"
  "chibig5/san2005.htm|37_二零零五年舊金山法會講法"
  "chibig5/la2006.htm|38_洛杉磯市法會講法"
  "chibig5/hy3_001.htm|39_洪吟三"
  "chibig5/jjyz3.htm|40_精進要旨三"
  "chibig5/jiangfa8.htm|41_各地講法八"
  "chibig5/jiangfa9.htm|42_各地講法九"
  "chibig5/jiangfa10.htm|43_各地講法十"
  "chibig5/jiangfa11.htm|44_各地講法十一"
  "chibig5/hy4/hy4-001.htm|45_洪吟四"
  "chibig5/hy5/big5/web-20190618/hy5-001.htm|46_洪吟五"
  "chibig5/jiangfa12.htm|47_各地講法十二"
  "chibig5/jiangfa13.htm|48_各地講法十三"
  "chibig5/jiangfa14.htm|49_各地講法十四"
  "chibig5/jiangfa15.htm|50_各地講法十五"
  "chibig5/hy6/hy6-01.htm|51_洪吟六"
)

SUCCESS=0
FAIL=0

for entry in "${BOOKS[@]}"; do
  IFS='|' read -r path name <<< "$entry"
  url="${BASE_URL}/${path}"
  outfile="${OUT_DIR}/${name}.html"

  echo "Downloading [${name}] from ${url} ..."
  if curl -s -f -L --connect-timeout 15 --max-time 60 -o "$outfile" "$url"; then
    size=$(wc -c < "$outfile" | tr -d ' ')
    echo "  OK - ${size} bytes"
    SUCCESS=$((SUCCESS + 1))
  else
    echo "  FAILED"
    FAIL=$((FAIL + 1))
  fi
done

echo ""
echo "============================="
echo "Download complete!"
echo "Success: ${SUCCESS} / $((SUCCESS + FAIL))"
echo "Failed:  ${FAIL} / $((SUCCESS + FAIL))"
echo "============================="

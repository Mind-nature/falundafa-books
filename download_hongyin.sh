#!/bin/bash
ROOT="D:/WORKCL/falundafa_books"
SUCCESS=0
FAIL=0

# 洪吟四: 150 pages
echo "=== 洪吟四 (150 pages) ==="
dir="$ROOT/45_hongyin4"
mkdir -p "$dir"
for i in $(seq -f "%03g" 1 150); do
  url="https://big5.falundafa.org/chibig5/hy4/hy4-${i}.htm"
  out="$dir/hy4-${i}.htm"
  if [ -f "$out" ]; then continue; fi
  if curl -s -L --connect-timeout 15 --max-time 60 -o "$out" "$url" && [ -s "$out" ]; then
    SUCCESS=$((SUCCESS + 1))
  else
    echo "  FAILED: hy4-${i}.htm"
    FAIL=$((FAIL + 1))
  fi
done
echo "  Done."

# 洪吟五: 80 pages
echo "=== 洪吟五 (80 pages) ==="
dir="$ROOT/46_hongyin5"
mkdir -p "$dir"
for i in $(seq -f "%03g" 1 80); do
  url="https://big5.falundafa.org/chibig5/hy5/big5/web-20190618/hy5-${i}.htm"
  out="$dir/hy5-${i}.htm"
  if [ -f "$out" ]; then continue; fi
  if curl -s -L --connect-timeout 15 --max-time 60 -o "$out" "$url" && [ -s "$out" ]; then
    SUCCESS=$((SUCCESS + 1))
  else
    echo "  FAILED: hy5-${i}.htm"
    FAIL=$((FAIL + 1))
  fi
done
echo "  Done."

# 洪吟六: 50 pages (2-digit numbering)
echo "=== 洪吟六 (50 pages) ==="
dir="$ROOT/51_hongyin6"
mkdir -p "$dir"
for i in $(seq -w 1 50); do
  url="https://big5.falundafa.org/chibig5/hy6/hy6-${i}.htm"
  out="$dir/hy6-${i}.htm"
  if [ -f "$out" ]; then continue; fi
  if curl -s -L --connect-timeout 15 --max-time 60 -o "$out" "$url" && [ -s "$out" ]; then
    SUCCESS=$((SUCCESS + 1))
  else
    echo "  FAILED: hy6-${i}.htm"
    FAIL=$((FAIL + 1))
  fi
done
echo "  Done."

echo ""
echo "============================="
echo "洪吟 download complete!"
echo "Success: $SUCCESS"
echo "Failed:  $FAIL"
echo "============================="

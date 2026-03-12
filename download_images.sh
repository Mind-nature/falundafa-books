#!/bin/bash
ROOT="D:/WORKCL/falundafa_books"
BASE="https://big5.falundafa.org"
SUCCESS=0
FAIL=0

dl() {
  local url="$1" out="$2"
  if [ -f "$out" ] && [ -s "$out" ]; then return 0; fi
  mkdir -p "$(dirname "$out")"
  if curl -s -L --connect-timeout 15 --max-time 60 -o "$out" "$url" && [ -s "$out" ]; then
    SUCCESS=$((SUCCESS + 1))
  else
    echo "  FAIL: $url"
    rm -f "$out"
    FAIL=$((FAIL + 1))
  fi
}

# 1. Navigation icons in chibig5/
echo "=== Navigation icons ==="
for icon in up.gif left.gif right.gif 1pix.gif; do
  dl "$BASE/chibig5/$icon" "$ROOT/chibig5/$icon"
done

# 2. hy3pic (洪吟三) - 141 images
echo "=== hy3pic (洪吟三 images) ==="
while IFS= read -r img; do
  dl "$BASE/chibig5/$img" "$ROOT/chibig5/$img"
done < <(grep 'hy3pic/' /tmp/all_img_refs.txt)

# 3. hypic (洪吟一/二) - 82 images
echo "=== hypic (洪吟一/二 images) ==="
while IFS= read -r img; do
  dl "$BASE/chibig5/$img" "$ROOT/chibig5/$img"
done < <(grep 'hypic/' /tmp/all_img_refs.txt)

# 4. chibig5/images/ (法輪功, 大圓滿法, 精進要旨二 etc.) - 189 images
echo "=== chibig5/images/ ==="
while IFS= read -r img; do
  dl "$BASE/chibig5/$img" "$ROOT/chibig5/$img"
done < /tmp/chibig5_images.txt

# 5. hy4/images/ (洪吟四) - 150 images
echo "=== hy4/images/ (洪吟四) ==="
while IFS= read -r img; do
  dl "$BASE/chibig5/hy4/$img" "$ROOT/45_hongyin4/$img"
done < /tmp/hy4_images.txt

# 6. hy5/images/ (洪吟五) - 80 images
echo "=== hy5/images/ (洪吟五) ==="
while IFS= read -r img; do
  dl "$BASE/chibig5/hy5/big5/web-20190618/$img" "$ROOT/46_hongyin5/$img"
done < /tmp/hy5_images.txt

# 7. hy6/images/ (洪吟六) - 50 images
echo "=== hy6/images/ (洪吟六) ==="
while IFS= read -r img; do
  dl "$BASE/chibig5/hy6/$img" "$ROOT/51_hongyin6/$img"
done < /tmp/hy6_images.txt

echo ""
echo "============================="
echo "Image download complete!"
echo "Success: $SUCCESS"
echo "Failed:  $FAIL"
echo "============================="

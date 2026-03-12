#!/bin/bash
# Fix all image src paths for offline browsing
ROOT="D:/WORKCL/falundafa_books"
FIXED=0

fix_sed() {
  local file="$1"
  shift
  local tmpfile="${file}.tmp"
  cp "$file" "$tmpfile"
  for expr in "$@"; do
    sed -i "$expr" "$tmpfile" 2>/dev/null
  done
  if ! cmp -s "$file" "$tmpfile"; then
    mv "$tmpfile" "$file"
    FIXED=$((FIXED + 1))
  else
    rm -f "$tmpfile"
  fi
}

# ============================================================
# GROUP 1: Root-level .html index pages
# Originally at chibig5/ → icons/images need chibig5/ prefix
# ============================================================
echo "=== Fixing root-level .html index pages ==="

for f in "$ROOT"/*.html; do
  [ -f "$f" ] || continue
  fix_sed "$f" \
    's|src="\.\./\.\./\.\./up\.gif"|src="chibig5/up.gif"|g' \
    's|src="\.\./\.\./\.\./left\.gif"|src="chibig5/left.gif"|g' \
    's|src="\.\./\.\./\.\./right\.gif"|src="chibig5/right.gif"|g' \
    's|src="\.\./up\.gif"|src="chibig5/up.gif"|g' \
    's|src="\.\./left\.gif"|src="chibig5/left.gif"|g' \
    's|src="\.\./right\.gif"|src="chibig5/right.gif"|g' \
    's|src="up\.gif"|src="chibig5/up.gif"|g' \
    's|src="left\.gif"|src="chibig5/left.gif"|g' \
    's|src="right\.gif"|src="chibig5/right.gif"|g' \
    's|src="1pix\.gif"|src="chibig5/1pix.gif"|g' \
    's|src="hypic/|src="chibig5/hypic/|g' \
    's|src="hy3pic/|src="chibig5/hy3pic/|g' \
    's|src="images/hy4_Page_|src="45_hongyin4/images/hy4_Page_|g' \
    's|src="images/hy5_Page_|src="46_hongyin5/images/hy5_Page_|g' \
    's|src="images/hy6_Page_|src="51_hongyin6/images/hy6_Page_|g'
done
echo "  Root index pages done. Fixed so far: $FIXED"

# ============================================================
# GROUP 2: Standard book sub-pages
# (all subdirs except chibig5, hongyin4/5/6, book08/31/32/49)
# Originally at chibig5/ → need ../chibig5/ prefix
# ============================================================
echo "=== Fixing standard book sub-pages ==="

for dir in "$ROOT"/*/; do
  dname=$(basename "$dir")
  # Skip special directories
  case "$dname" in
    chibig5|45_hongyin4|46_hongyin5|51_hongyin6|book08|book31|book32|book49) continue ;;
  esac

  for f in "$dir"*.htm; do
    [ -f "$f" ] || continue
    fix_sed "$f" \
      's|src="up\.gif"|src="../chibig5/up.gif"|g' \
      's|src="left\.gif"|src="../chibig5/left.gif"|g' \
      's|src="right\.gif"|src="../chibig5/right.gif"|g' \
      's|src="1pix\.gif"|src="../chibig5/1pix.gif"|g' \
      's|src="images/|src="../chibig5/images/|g' \
      's|src="hy3pic/|src="../chibig5/hy3pic/|g' \
      's|src="hypic/|src="../chibig5/hypic/|g'
  done
done
echo "  Standard sub-pages done. Fixed so far: $FIXED"

# ============================================================
# GROUP 3: hongyin4/5/6 sub-pages
# images/ is already correct, only fix navigation icons
# ============================================================
echo "=== Fixing hongyin4/5/6 navigation icons ==="

# 45_hongyin4: nav icons use ../
for f in "$ROOT/45_hongyin4/"*.htm; do
  [ -f "$f" ] || continue
  fix_sed "$f" \
    's|src="\.\./up\.gif"|src="../chibig5/up.gif"|g' \
    's|src="\.\./left\.gif"|src="../chibig5/left.gif"|g' \
    's|src="\.\./right\.gif"|src="../chibig5/right.gif"|g' \
    's|src="up\.gif"|src="../chibig5/up.gif"|g' \
    's|src="left\.gif"|src="../chibig5/left.gif"|g' \
    's|src="right\.gif"|src="../chibig5/right.gif"|g'
done

# 46_hongyin5: nav icons use ../../../
for f in "$ROOT/46_hongyin5/"*.htm; do
  [ -f "$f" ] || continue
  fix_sed "$f" \
    's|src="\.\./\.\./\.\./up\.gif"|src="../chibig5/up.gif"|g' \
    's|src="\.\./\.\./\.\./left\.gif"|src="../chibig5/left.gif"|g' \
    's|src="\.\./\.\./\.\./right\.gif"|src="../chibig5/right.gif"|g' \
    's|src="up\.gif"|src="../chibig5/up.gif"|g' \
    's|src="left\.gif"|src="../chibig5/left.gif"|g' \
    's|src="right\.gif"|src="../chibig5/right.gif"|g'
done

# 51_hongyin6: nav icons use ../
for f in "$ROOT/51_hongyin6/"*.htm; do
  [ -f "$f" ] || continue
  fix_sed "$f" \
    's|src="\.\./up\.gif"|src="../chibig5/up.gif"|g' \
    's|src="\.\./left\.gif"|src="../chibig5/left.gif"|g' \
    's|src="\.\./right\.gif"|src="../chibig5/right.gif"|g' \
    's|src="up\.gif"|src="../chibig5/up.gif"|g' \
    's|src="left\.gif"|src="../chibig5/left.gif"|g' \
    's|src="right\.gif"|src="../chibig5/right.gif"|g'
done
echo "  Hongyin 4/5/6 done. Fixed so far: $FIXED"

# ============================================================
# GROUP 4: book08/31/32/49 sub-pages
# Originally at chibig5/ → need ../chibig5/ prefix
# ============================================================
echo "=== Fixing book08/31/32/49 sub-pages ==="

for bdir in book08 book31 book32 book49; do
  for f in "$ROOT/$bdir/"*.htm; do
    [ -f "$f" ] || continue
    fix_sed "$f" \
      's|src="up\.gif"|src="../chibig5/up.gif"|g' \
      's|src="left\.gif"|src="../chibig5/left.gif"|g' \
      's|src="right\.gif"|src="../chibig5/right.gif"|g' \
      's|src="1pix\.gif"|src="../chibig5/1pix.gif"|g' \
      's|src="images/|src="../chibig5/images/|g'
  done
done
echo "  Book08/31/32/49 done. Fixed so far: $FIXED"

# ============================================================
# GROUP 5: Fix href navigation links in root index pages
# e.g., href="zfl_01.htm" → href="01_轉法輪/zfl_01.htm"
# ============================================================
echo "=== Fixing href navigation links in index pages ==="

# Build sed expressions: for each .htm in a subdirectory,
# rewrite href in the corresponding root .html
for dir in "$ROOT"/*/; do
  dname=$(basename "$dir")
  [ "$dname" = "chibig5" ] && continue

  for htmfile in "$dir"*.htm; do
    [ -f "$htmfile" ] || continue
    htmname=$(basename "$htmfile")
    # Find which root .html references this .htm
    for roothtml in "$ROOT"/*.html; do
      if grep -q "href=\"$htmname\"" "$roothtml" 2>/dev/null; then
        sed -i "s|href=\"$htmname\"|href=\"$dname/$htmname\"|g" "$roothtml" 2>/dev/null
      fi
    done
  done
done
echo "  Href links done."

echo ""
echo "============================="
echo "  Path fix complete!"
echo "  Total files modified: $FIXED+"
echo "============================="

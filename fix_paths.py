"""
Fix all image (and navigation icon) src paths in downloaded HTML files
so that offline browsing works correctly.

Directory structure:
  falundafa_books/
  ├── *.html              (51 index pages, originally at chibig5/)
  ├── 01_轉法輪/           (sub-pages, originally at chibig5/)
  ├── 02_法輪功/           ...
  ├── ... (more book subdirs)
  ├── 45_hongyin4/         (originally at chibig5/hy4/)
  │   ├── *.htm
  │   └── images/          (hy4 images - already correct relative path)
  ├── 46_hongyin5/         (originally at chibig5/hy5/big5/web-20190618/)
  │   ├── *.htm
  │   └── images/          (hy5 images - already correct)
  ├── 51_hongyin6/         (originally at chibig5/hy6/)
  │   ├── *.htm
  │   └── images/          (hy6 images - already correct)
  ├── book08/, book31/, book32/, book49/  (sub-pages, originally at chibig5/)
  └── chibig5/
      ├── up.gif, left.gif, right.gif, 1pix.gif
      ├── hy3pic/          (洪吟三 images)
      ├── hypic/           (洪吟一/二 images)
      └── images/          (general book images)
"""

import os
import re
import glob

ROOT = r"D:/WORKCL/falundafa_books"
fixed_count = 0
file_count = 0


def fix_file(filepath, replacements):
    """Apply a list of (pattern, replacement) regex substitutions to a file."""
    global fixed_count, file_count
    with open(filepath, "rb") as f:
        content = f.read()

    original = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)

    if content != original:
        with open(filepath, "wb") as f:
            f.write(content)
        changes = sum(1 for p, r in replacements
                      if re.search(p, original))
        fixed_count += 1
        return True
    return False


# ============================================================
# GROUP 1: Root-level .html files (51 index pages)
# Originally at chibig5/ on the server
# ============================================================
print("=== Fixing root-level .html index pages ===")

root_htmls = glob.glob(os.path.join(ROOT, "*.html"))
g1_count = 0

for fpath in root_htmls:
    fname = os.path.basename(fpath)

    replacements = [
        # Navigation icons: various relative paths → chibig5/
        (rb'src="\.\./\.\./\.\./up\.gif"', b'src="chibig5/up.gif"'),
        (rb'src="\.\./\.\./\.\./left\.gif"', b'src="chibig5/left.gif"'),
        (rb'src="\.\./\.\./\.\./right\.gif"', b'src="chibig5/right.gif"'),
        (rb'src="\.\./up\.gif"', b'src="chibig5/up.gif"'),
        (rb'src="\.\./left\.gif"', b'src="chibig5/left.gif"'),
        (rb'src="\.\./right\.gif"', b'src="chibig5/right.gif"'),
        (rb'src="up\.gif"', b'src="chibig5/up.gif"'),
        (rb'src="left\.gif"', b'src="chibig5/left.gif"'),
        (rb'src="right\.gif"', b'src="chibig5/right.gif"'),
        (rb'src="1pix\.gif"', b'src="chibig5/1pix.gif"'),
        # hypic/ and hy3pic/ → chibig5/
        (rb'src="hypic/', b'src="chibig5/hypic/'),
        (rb'src="hy3pic/', b'src="chibig5/hy3pic/'),
    ]

    # Special handling for 洪吟四/五/六 index pages (images/ → their own subdir)
    with open(fpath, "rb") as f:
        content = f.read()

    if b"hy4_Page_" in content:
        replacements.append(
            (rb'src="images/(hy4_Page_[^"]+)"', rb'src="45_hongyin4/images/\1"'))
    elif b"hy5_Page_" in content:
        replacements.append(
            (rb'src="images/(hy5_Page_[^"]+)"', rb'src="46_hongyin5/images/\1"'))
    elif b"hy6_Page_" in content:
        replacements.append(
            (rb'src="images/(hy6_Page_[^"]+)"', rb'src="51_hongyin6/images/\1"'))

    if fix_file(fpath, replacements):
        g1_count += 1

print(f"  Fixed {g1_count}/{len(root_htmls)} files")


# ============================================================
# GROUP 2: Standard book sub-page .htm files
# (01_轉法輪/, 02_法輪功/, ... etc.)
# Originally at chibig5/ on the server
# ============================================================
print("=== Fixing standard book sub-pages ===")

# These directories contain sub-pages originally at chibig5/
standard_dirs = [
    d for d in glob.glob(os.path.join(ROOT, "*/"))
    if os.path.basename(os.path.normpath(d)) not in
    ("chibig5", "45_hongyin4", "46_hongyin5", "51_hongyin6",
     "book08", "book31", "book32", "book49")
]

g2_count = 0
g2_total = 0

for dirpath in standard_dirs:
    htm_files = glob.glob(os.path.join(dirpath, "*.htm"))
    g2_total += len(htm_files)

    for fpath in htm_files:
        replacements = [
            # Navigation icons → ../chibig5/
            (rb'src="up\.gif"', b'src="../chibig5/up.gif"'),
            (rb'src="left\.gif"', b'src="../chibig5/left.gif"'),
            (rb'src="right\.gif"', b'src="../chibig5/right.gif"'),
            (rb'src="1pix\.gif"', b'src="../chibig5/1pix.gif"'),
            # images/ → ../chibig5/images/
            (rb'src="images/', b'src="../chibig5/images/'),
            # hy3pic/ → ../chibig5/hy3pic/
            (rb'src="hy3pic/', b'src="../chibig5/hy3pic/'),
            # hypic/ → ../chibig5/hypic/
            (rb'src="hypic/', b'src="../chibig5/hypic/'),
        ]
        if fix_file(fpath, replacements):
            g2_count += 1

print(f"  Fixed {g2_count}/{g2_total} files")


# ============================================================
# GROUP 3: hongyin4/5/6 sub-pages
# images/ paths are already correct, only fix navigation icons
# ============================================================
print("=== Fixing hongyin4/5/6 sub-pages ===")

g3_count = 0
g3_total = 0

# 45_hongyin4: originally at chibig5/hy4/, nav icons use ../
for fpath in glob.glob(os.path.join(ROOT, "45_hongyin4", "*.htm")):
    g3_total += 1
    replacements = [
        (rb'src="\.\./up\.gif"', b'src="../chibig5/up.gif"'),
        (rb'src="\.\./left\.gif"', b'src="../chibig5/left.gif"'),
        (rb'src="\.\./right\.gif"', b'src="../chibig5/right.gif"'),
        (rb'src="up\.gif"', b'src="../chibig5/up.gif"'),
        (rb'src="left\.gif"', b'src="../chibig5/left.gif"'),
        (rb'src="right\.gif"', b'src="../chibig5/right.gif"'),
    ]
    if fix_file(fpath, replacements):
        g3_count += 1

# 46_hongyin5: originally at chibig5/hy5/big5/web-20190618/, nav icons use ../../../
for fpath in glob.glob(os.path.join(ROOT, "46_hongyin5", "*.htm")):
    g3_total += 1
    replacements = [
        (rb'src="\.\./\.\./\.\./up\.gif"', b'src="../chibig5/up.gif"'),
        (rb'src="\.\./\.\./\.\./left\.gif"', b'src="../chibig5/left.gif"'),
        (rb'src="\.\./\.\./\.\./right\.gif"', b'src="../chibig5/right.gif"'),
        (rb'src="up\.gif"', b'src="../chibig5/up.gif"'),
        (rb'src="left\.gif"', b'src="../chibig5/left.gif"'),
        (rb'src="right\.gif"', b'src="../chibig5/right.gif"'),
    ]
    if fix_file(fpath, replacements):
        g3_count += 1

# 51_hongyin6: originally at chibig5/hy6/, nav icons use ../
for fpath in glob.glob(os.path.join(ROOT, "51_hongyin6", "*.htm")):
    g3_total += 1
    replacements = [
        (rb'src="\.\./up\.gif"', b'src="../chibig5/up.gif"'),
        (rb'src="\.\./left\.gif"', b'src="../chibig5/left.gif"'),
        (rb'src="\.\./right\.gif"', b'src="../chibig5/right.gif"'),
        (rb'src="up\.gif"', b'src="../chibig5/up.gif"'),
        (rb'src="left\.gif"', b'src="../chibig5/left.gif"'),
        (rb'src="right\.gif"', b'src="../chibig5/right.gif"'),
    ]
    if fix_file(fpath, replacements):
        g3_count += 1

print(f"  Fixed {g3_count}/{g3_total} files")


# ============================================================
# GROUP 4: book08, book31, book32, book49 sub-pages
# Originally at chibig5/ on the server
# ============================================================
print("=== Fixing book08/31/32/49 sub-pages ===")

g4_count = 0
g4_total = 0

for bdir in ["book08", "book31", "book32", "book49"]:
    for fpath in glob.glob(os.path.join(ROOT, bdir, "*.htm")):
        g4_total += 1
        replacements = [
            (rb'src="up\.gif"', b'src="../chibig5/up.gif"'),
            (rb'src="left\.gif"', b'src="../chibig5/left.gif"'),
            (rb'src="right\.gif"', b'src="../chibig5/right.gif"'),
            (rb'src="1pix\.gif"', b'src="../chibig5/1pix.gif"'),
            (rb'src="images/', b'src="../chibig5/images/'),
        ]
        if fix_file(fpath, replacements):
            g4_count += 1

print(f"  Fixed {g4_count}/{g4_total} files")


# ============================================================
# ALSO: Fix href navigation links between pages
# (so prev/next page links work offline)
# ============================================================
print("=== Fixing href navigation links in index pages ===")

# Root-level index pages have href links to sub-pages like "zfl_01.htm"
# These need to point into the correct subdirectory
# e.g., in 01_轉法輪.html: href="zfl_01.htm" → href="01_轉法輪/zfl_01.htm"

# Build a mapping of .htm filename → subdirectory
htm_to_dir = {}
for dirpath in glob.glob(os.path.join(ROOT, "*/")):
    dirname = os.path.basename(os.path.normpath(dirpath))
    if dirname == "chibig5":
        continue
    for htmfile in glob.glob(os.path.join(dirpath, "*.htm")):
        htmname = os.path.basename(htmfile)
        htm_to_dir[htmname] = dirname

g5_count = 0
for fpath in root_htmls:
    with open(fpath, "rb") as f:
        content = f.read()

    original = content

    # Find all href="xxx.htm" references
    for match in re.finditer(rb'href="([^"/]+\.htm)"', original):
        htmname = match.group(1).decode("utf-8", errors="replace")
        if htmname in htm_to_dir:
            old = match.group(0)
            new = f'href="{htm_to_dir[htmname]}/{htmname}"'.encode("utf-8")
            content = content.replace(old, new, 1)

    if content != original:
        with open(fpath, "wb") as f:
            f.write(content)
        g5_count += 1

print(f"  Fixed {g5_count}/{len(root_htmls)} index pages with href links")


# ============================================================
# Summary
# ============================================================
print()
print("=" * 50)
print(f"  Total files modified: {fixed_count + g5_count}")
print("=" * 50)

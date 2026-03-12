"""
Fix all uppercase SRC= image paths for navigation icons (up.gif, left.gif, right.gif, 1pix.gif)
Handles SRC=, Src=, and any case variation.
"""
import os
import re
import glob

ROOT = r"D:/WORKCL/falundafa_books"

def fix_file(filepath, replacements):
    """Apply regex replacements to a file. Returns True if modified."""
    with open(filepath, "rb") as f:
        content = f.read()
    original = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
    if content != original:
        with open(filepath, "wb") as f:
            f.write(content)
        return True
    return False

# ============================================================
# GROUP 1: Root-level .html files
# Icons should point to chibig5/xxx.gif
# ============================================================
print("=== Fixing root-level .html files (case-insensitive) ===")
g1 = 0
for fpath in glob.glob(os.path.join(ROOT, "*.html")):
    replacements = [
        # Any case SRC="up.gif" → SRC="chibig5/up.gif"  (but not if already has chibig5/)
        (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?up\.gif"', rb'\1chibig5/up.gif"'),
        (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?left\.gif"', rb'\1chibig5/left.gif"'),
        (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?right\.gif"', rb'\1chibig5/right.gif"'),
        (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?1pix\.gif"', rb'\1chibig5/1pix.gif"'),
    ]
    if fix_file(fpath, replacements):
        g1 += 1
print(f"  Fixed {g1} files")

# ============================================================
# GROUP 2: Sub-page .htm files in standard book directories
# Icons should point to ../chibig5/xxx.gif
# ============================================================
print("=== Fixing sub-page .htm files (case-insensitive) ===")
g2 = 0
g2_total = 0

for dirpath in glob.glob(os.path.join(ROOT, "*/")):
    dirname = os.path.basename(os.path.normpath(dirpath))
    if dirname == "chibig5":
        continue

    for fpath in glob.glob(os.path.join(dirpath, "*.htm")):
        g2_total += 1
        replacements = [
            # Any case SRC="up.gif" or SRC="../up.gif" etc → SRC="../chibig5/up.gif"
            (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?up\.gif"', rb'\1../chibig5/up.gif"'),
            (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?left\.gif"', rb'\1../chibig5/left.gif"'),
            (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?right\.gif"', rb'\1../chibig5/right.gif"'),
            (rb'(?i)(SRC=")(?:\.\./)*(?:\.\./\.\./)?1pix\.gif"', rb'\1../chibig5/1pix.gif"'),
        ]
        if fix_file(fpath, replacements):
            g2 += 1

print(f"  Fixed {g2}/{g2_total} files")

print()
print("=" * 50)
print(f"  Total files modified: {g1 + g2}")
print("=" * 50)

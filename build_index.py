"""
Scan all 51 books and generate a JSON index file.
For each book: name, chapters (name + file path).
Handles both TOC-style books (with subdirectories) and single-page books.
"""
import os
import re
import json
import glob

ROOT = r"D:/WORKCL/falundafa_books"

# Ordered list of all 51 books with their index HTML and subdirectory
BOOKS = [
    (1, "轉法輪", "01_轉法輪.html", "01_轉法輪"),
    (2, "法輪功", "02_法輪功.html", "02_法輪功"),
    (3, "法輪大法義解", "03_法輪大法義解.html", "03_法輪大法義解"),
    (4, "轉法輪法解", "04_轉法輪法解.html", "04_轉法輪法解"),
    (5, "轉法輪（卷二）", "05_轉法輪卷二.html", "05_轉法輪卷二"),
    (6, "悉尼法會講法", "06_悉尼法會講法.html", None),
    (7, "大圓滿法", "07_大圓滿法.html", "07_大圓滿法"),
    (8, "美國法會講法", "08_美國法會講法.html", "08_美國法會講法"),
    (9, "精進要旨", "09_精進要旨.html", "09_精進要旨"),
    (10, "北美首屆法會講法", "10_北美首屆法會講法.html", None),
    (11, "歐洲法會講法", "11_歐洲法會講法.html", None),
    (12, "長春輔導員法會講法", "12_長春輔導員法會講法.html", None),
    (13, "新加坡法會講法", "13_新加坡法會講法.html", None),
    (14, "瑞士法會講法", "14_瑞士法會講法.html", None),
    (15, "洪吟", "15_洪吟.html", None),
    (16, "美國西部法會講法", "16_美國西部法會講法.html", None),
    (17, "美國東部法會講法", "17_美國東部法會講法.html", None),
    (18, "澳大利亞法會講法", "18_澳大利亞法會講法.html", None),
    (19, "新西蘭法會講法", "19_新西蘭法會講法.html", None),
    (20, "加拿大法會講法", "20_加拿大法會講法.html", None),
    (21, "美國中部法會講法", "21_美國中部法會講法.html", None),
    (22, "導航", "22_導航.html", "22_導航"),
    (23, "精進要旨二", "23_精進要旨二.html", "23_精進要旨二"),
    (24, "北美巡迴講法", "24_北美巡迴講法.html", None),
    (25, "二零零三年元宵節講法", "25_二零零三年元宵節講法.html", None),
    (26, "洪吟二", "26_洪吟二.html", None),
    (27, "休斯頓法會講法", "27_休斯頓法會講法.html", None),
    (28, "各地講法一", "28_各地講法一.html", "28_各地講法一"),
    (29, "各地講法二", "29_各地講法二.html", "29_各地講法二"),
    (30, "各地講法三", "30_各地講法三.html", "30_各地講法三"),
    (31, "音樂與美術創作會講法", "31_音樂與美術創作會講法.html", "31_音樂與美術創作會講法"),
    (32, "各地講法四", "32_各地講法四.html", "32_各地講法四"),
    (33, "各地講法五", "33_各地講法五.html", "33_各地講法五"),
    (34, "各地講法六", "34_各地講法六.html", "34_各地講法六"),
    (35, "二零零四年紐約國際法會講法", "35_二零零四年紐約國際法會講法.html", None),
    (36, "各地講法七", "36_各地講法七.html", "36_各地講法七"),
    (37, "二零零五年舊金山法會講法", "37_二零零五年舊金山法會講法.html", None),
    (38, "洛杉磯市法會講法", "38_洛杉磯市法會講法.html", None),
    (39, "洪吟三", "39_洪吟三.html", "39_洪吟三"),
    (40, "精進要旨三", "40_精進要旨三.html", "40_精進要旨三"),
    (41, "各地講法八", "41_各地講法八.html", "41_各地講法八"),
    (42, "各地講法九", "42_各地講法九.html", "42_各地講法九"),
    (43, "各地講法十", "43_各地講法十.html", "43_各地講法十"),
    (44, "各地講法十一", "44_各地講法十一.html", "44_各地講法十一"),
    (45, "洪吟四", "45_洪吟四.html", "45_hongyin4"),
    (46, "洪吟五", "46_洪吟五.html", "46_hongyin5"),
    (47, "各地講法十二", "47_各地講法十二.html", "47_各地講法十二"),
    (48, "各地講法十三", "48_各地講法十三.html", "48_各地講法十三"),
    (49, "各地講法十四", "49_各地講法十四.html", "49_各地講法十四"),
    (50, "各地講法十五", "50_各地講法十五.html", "50_各地講法十五"),
    (51, "洪吟六", "51_洪吟六.html", "51_hongyin6"),
]


def extract_chapter_names_from_index(index_path, subdir):
    """Extract chapter names and file paths from an index HTML page."""
    chapters = []
    with open(index_path, "rb") as f:
        content = f.read().decode("utf-8", errors="replace")

    # Find all href links to .htm files (not ../ links)
    seen = set()
    for m in re.finditer(r'href="([^"]*\.htm)"', content):
        href = m.group(1)
        # Skip parent directory links
        if href.startswith(".."):
            continue
        # Get the actual filename (might have subdir prefix)
        fname = href.split("/")[-1]
        if fname in seen:
            continue
        seen.add(fname)

        # Try to extract the link text (chapter name)
        # Look for text after the closing > tag
        pos = m.end()
        # Find the text between > and <
        text_match = re.search(r'>([^<]+)<', content[pos:pos+200])
        if text_match:
            name = text_match.group(1).strip()
            # Skip if it's just whitespace or navigation text
            if name and name not in ("　", " ", ""):
                # Build the file path
                if subdir:
                    filepath = f"{subdir}/{fname}"
                else:
                    filepath = fname
                chapters.append({"name": name, "file": filepath})

    return chapters


def extract_title_from_content(content):
    """Try to extract a title from HTML content."""
    # Try <title> tag
    m = re.search(r'<title>([^<]+)</title>', content, re.I)
    if m:
        return m.group(1).strip()
    # Try first <h1> or <h2>
    m = re.search(r'<h[12][^>]*>([^<]+)</h[12]>', content, re.I)
    if m:
        return m.group(1).strip()
    return None


def build_index():
    result = []

    for book_id, name, index_file, subdir in BOOKS:
        index_path = os.path.join(ROOT, index_file)

        # Check if index file exists (handle possible name encoding issues)
        if not os.path.exists(index_path):
            # Try to find it by glob
            pattern = os.path.join(ROOT, f"{book_id:02d}_*.html")
            matches = glob.glob(pattern)
            if matches:
                index_path = matches[0]
                index_file = os.path.basename(index_path)
            else:
                print(f"WARNING: Index not found for {book_id}. {name}")
                result.append({"id": book_id, "name": name, "type": "missing", "chapters": []})
                continue

        # Check if this is a multi-chapter book (has a subdirectory)
        if subdir and os.path.isdir(os.path.join(ROOT, subdir)):
            chapters = extract_chapter_names_from_index(index_path, subdir)
            if chapters:
                result.append({
                    "id": book_id,
                    "name": name,
                    "type": "multi",
                    "chapters": chapters
                })
            else:
                # Subdirectory exists but no chapters extracted from index
                # Scan the subdirectory directly
                htm_files = sorted(glob.glob(os.path.join(ROOT, subdir, "*.htm")))
                chapters = []
                for hf in htm_files:
                    fname = os.path.basename(hf)
                    # Skip the index copy
                    if fname in (index_file.replace(".html", ".htm"),):
                        continue
                    with open(hf, "rb") as f:
                        c = f.read().decode("utf-8", errors="replace")
                    title = extract_title_from_content(c) or fname
                    chapters.append({"name": title, "file": f"{subdir}/{fname}"})
                result.append({
                    "id": book_id,
                    "name": name,
                    "type": "multi",
                    "chapters": chapters
                })
        else:
            # Single-page book - the index file IS the content
            result.append({
                "id": book_id,
                "name": name,
                "type": "single",
                "file": index_file,
                "chapters": []
            })

    # Fix: if all chapters in a book have the same name, use page numbers
    for book in result:
        chapters = book.get("chapters", [])
        if len(chapters) > 1:
            names = set(ch["name"] for ch in chapters)
            if len(names) == 1:
                for i, ch in enumerate(chapters):
                    ch["name"] = f"第 {i+1} 頁"

    return result


if __name__ == "__main__":
    index = build_index()

    # Write JSON
    out_path = os.path.join(ROOT, "books_index.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    # Summary
    multi = sum(1 for b in index if b["type"] == "multi")
    single = sum(1 for b in index if b["type"] == "single")
    total_ch = sum(len(b["chapters"]) for b in index)
    print(f"Generated {out_path}")
    print(f"  Books: {len(index)} ({multi} multi-chapter, {single} single-page)")
    print(f"  Total chapters: {total_ch}")

    # Show first 3 books as sample
    for b in index[:3]:
        print(f"\n  [{b['id']}] {b['name']} ({b['type']})")
        for ch in b["chapters"][:5]:
            print(f"    - {ch['name']} -> {ch['file']}")
        if len(b["chapters"]) > 5:
            print(f"    ... and {len(b['chapters'])-5} more")

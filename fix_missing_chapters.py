import json, re

# Missing first chapters: (book_id, chapter_name, chapter_file)
missing = [
    # Already fixed: (1, "論語", "01_轉法輪/zfl_01.htm"), (2, "第一章　概論", "02_法輪功/flg_1.htm")
    (3, "為長春法輪大法輔導員講法", "03_法輪大法義解/yijie_1.htm"),
    (4, "北京《轉法輪》首發式上講法", "04_轉法輪法解/fajie_1.htm"),
    (5, "在大嶼山講法", "05_轉法輪卷二/zfl2_01.htm"),
    (7, "一、功法特點", "07_大圓滿法/dymf_1.htm"),
    (8, "紐約法會講法", "08_美國法會講法/mgjf_1.htm"),
    (9, "論語", "09_精進要旨/jjyz_01.htm"),
    (22, "美國西部法會講法", "22_導航/daohang_1.htm"),
    (23, "見真性", "23_精進要旨二/jjyz2_01.htm"),
    (28, "新加坡佛學會成立典禮講法", "28_各地講法一/jiangfa1_1.htm"),
    (29, "美國佛羅里達法會講法", "29_各地講法二/jiangfa2_1.htm"),
    (30, "大紐約地區法會講法", "30_各地講法三/jiangfa3_1.htm"),
    (31, "音樂創作會講法", "31_音樂與美術創作會講法/yyms_1.htm"),
    (32, "二零零三年華盛頓ＤＣ法會講法", "32_各地講法四/jiangfa4_1.htm"),
    (33, "二零零四年美國西部法會講法", "33_各地講法五/jiangfa5_1.htm"),
    (34, "二零零四年復活節紐約法會講法", "34_各地講法六/jiangfa6_1.htm"),
    (36, "美西國際法會講法", "36_各地講法七/jiangfa7_1.htm"),
    (40, "致紐約法會的賀詞", "40_精進要旨三/jjyz3_01.htm"),
    (41, "二零零七年紐約法會講法", "41_各地講法八/jiangfa8_1.htm"),
    (42, "二零零九年大紐約國際法會講法", "42_各地講法九/jiangfa9_1.htm"),
    (43, "在明慧網十週年法會上講法", "43_各地講法十/jiangfa10_1.htm"),
    (44, "二零一零年紐約法會講法", "44_各地講法十一/jiangfa11_1.htm"),
    (47, "二零一二年美國首都國際法會講法", "47_各地講法十二/jiangfa12_1.htm"),
    (48, "二零一四年舊金山法會講法", "48_各地講法十三/jiangfa13_1.htm"),
    (49, "二零一六年紐約法會講法", "49_各地講法十四/jiangfa14_1.htm"),
    (50, "二零一八年華盛頓ＤＣ講法", "50_各地講法十五/jiangfa15_1.htm"),
]

# Fix books_index.json
with open('books_index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

missing_by_id = {m[0]: (m[1], m[2]) for m in missing}

for book in data:
    if book['id'] in missing_by_id:
        name, file = missing_by_id[book['id']]
        new_ch = {"name": name, "file": file}
        book['chapters'].insert(0, new_ch)
        print(f"Fixed book {book['id']}: {book['name']} - added '{name}'")

with open('books_index.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Fix index.html BOOKS_DATA
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the BOOKS_DATA line and parse it
match = re.search(r'const BOOKS_DATA = (\[.*?\]);', html)
if match:
    books_data = json.loads(match.group(1))
    for book in books_data:
        if book['id'] in missing_by_id:
            name, file = missing_by_id[book['id']]
            new_ch = {"name": name, "file": file}
            book['chapters'].insert(0, new_ch)
    
    new_json = json.dumps(books_data, ensure_ascii=False)
    html = html[:match.start(1)] + new_json + html[match.end(1):]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("\nindex.html BOOKS_DATA updated!")
else:
    print("ERROR: Could not find BOOKS_DATA in index.html")

print("\nDone!")

# 統計 52 本書的正文字數，輸出可直接貼進 index.html 的 bookWordCounts 內容
# 規則：計漢字＋數字＋英文字母（含全形），不含標點、空格、換行；各講標題算入
# 來源：search-index.json 的正文（與站內搜尋同口徑）；索引缺的檔退回解析 HTML
# 用法：在 repo 根目錄執行 python3 tools/count_words.py
import json, re, html, os

os.chdir(os.path.join(os.path.dirname(__file__), '..'))
idx = json.load(open('search-index.json'))
books = json.load(open('books_index.json'))

COUNT_RE = re.compile(r'[0-9A-Za-z０-９Ａ-Ｚａ-ｚ〇㐀-䶿一-鿿豈-﫿\U00020000-\U0002FFFF]')

# 洪吟/洪吟二：books_index 指到的是整本文字版（含目錄），正文以索引分頁 key 為準
SPECIAL_PREFIX = {15: '15_hongyin/', 26: '26_hongyin2/'}

def html_text(path):
    raw = open(path, 'rb').read()
    for enc in ('utf-8', 'cp950', 'big5hkscs'):
        try:
            s = raw.decode(enc); break
        except UnicodeDecodeError:
            continue
    else:
        s = raw.decode('utf-8', 'replace')
    s = re.sub(r'(?is)<head\b.*?</head>', '', s)
    s = re.sub(r'(?is)<script\b.*?</script>', '', s)
    s = re.sub(r'(?is)<style\b.*?</style>', '', s)
    s = re.sub(r'(?s)<!--.*?-->', '', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return html.unescape(s)

final = {}
for b in books:
    bid = b['id']
    if bid in SPECIAL_PREFIX:
        total = sum(len(COUNT_RE.findall(t)) for k, t in idx.items()
                    if k.startswith(SPECIAL_PREFIX[bid]))
    else:
        files = [c['file'] for c in b.get('chapters', [])] if b['type'] == 'multi' else [b['file']]
        total = 0
        for f in files:
            t = idx.get(f)
            if t is None:
                t = html_text(f) if os.path.exists(f) else ''
            total += len(COUNT_RE.findall(t))
    final[bid] = total
    print(f"{bid:>2}  {total:>9,}  {b['name']}")

print('---')
print('總計:', f"{sum(final.values()):,}")
print()
print('貼進 index.html 的 bookWordCounts（0 字的書不列）：')
entries = [f"{k}:{v}" for k, v in sorted(final.items()) if v > 0]
for i in range(0, len(entries), 6):
    print('  ' + ','.join(entries[i:i+6]) + (',' if i + 6 < len(entries) else ''))

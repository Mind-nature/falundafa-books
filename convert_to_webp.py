"""
將洪吟系列的圖片轉換為 WebP 格式，並更新 htm 檔案中的引用。
"""
import os
import re
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))

# 定義每本書的圖片目錄和 htm 目錄
BOOKS = [
    {
        'name': '洪吟',
        'image_dir': os.path.join(BASE, '15_hongyin', 'images'),
        'htm_dir': os.path.join(BASE, '15_hongyin'),
        'ext': '.png',
    },
    {
        'name': '洪吟二',
        'image_dir': os.path.join(BASE, '26_hongyin2', 'images'),
        'htm_dir': os.path.join(BASE, '26_hongyin2'),
        'ext': '.png',
    },
    {
        'name': '洪吟三',
        'image_dir': os.path.join(BASE, 'chibig5', 'hy3pic'),
        'htm_dir': os.path.join(BASE, '39_洪吟三'),
        'ext': '.png',
    },
    {
        'name': '洪吟四',
        'image_dir': os.path.join(BASE, '45_hongyin4', 'images'),
        'htm_dir': os.path.join(BASE, '45_hongyin4'),
        'ext': '.png',
    },
    {
        'name': '洪吟五',
        'image_dir': os.path.join(BASE, '46_hongyin5', 'images'),
        'htm_dir': os.path.join(BASE, '46_hongyin5'),
        'ext': '.jpg',
    },
    {
        'name': '洪吟六',
        'image_dir': os.path.join(BASE, '51_hongyin6', 'images'),
        'htm_dir': os.path.join(BASE, '51_hongyin6'),
        'ext': '.jpg',
    },
]

WEBP_QUALITY = 85
total_saved = 0

for book in BOOKS:
    print(f"\n=== {book['name']} ===")
    img_dir = book['image_dir']
    htm_dir = book['htm_dir']
    ext = book['ext']
    book_saved = 0
    converted = 0

    # 1. 轉換圖片
    for fname in sorted(os.listdir(img_dir)):
        if not fname.lower().endswith(ext):
            continue
        src_path = os.path.join(img_dir, fname)
        webp_name = os.path.splitext(fname)[0] + '.webp'
        dst_path = os.path.join(img_dir, webp_name)

        orig_size = os.path.getsize(src_path)
        img = Image.open(src_path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(dst_path, 'WEBP', quality=WEBP_QUALITY)
        new_size = os.path.getsize(dst_path)

        saved = orig_size - new_size
        book_saved += saved
        converted += 1

    print(f"  轉換 {converted} 張圖片, 節省 {book_saved // 1024}KB")

    # 2. 更新 htm 檔案中的引用
    updated_files = 0
    for fname in sorted(os.listdir(htm_dir)):
        if not fname.lower().endswith('.htm'):
            continue
        htm_path = os.path.join(htm_dir, fname)
        with open(htm_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 替換 .png 或 .jpg 為 .webp（只替換圖片引用）
        new_content = re.sub(
            r'(src\s*=\s*"[^"]*?)' + re.escape(ext) + r'(")',
            r'\1.webp\2',
            content,
            flags=re.IGNORECASE
        )

        if new_content != content:
            with open(htm_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files += 1

    print(f"  更新 {updated_files} 個 htm 檔案")
    total_saved += book_saved

    # 3. 刪除原始圖片
    deleted = 0
    for fname in sorted(os.listdir(img_dir)):
        if fname.lower().endswith(ext):
            os.remove(os.path.join(img_dir, fname))
            deleted += 1
    print(f"  刪除 {deleted} 張原始 {ext} 圖片")

print(f"\n=== 完成 ===")
print(f"總共節省: {total_saved // 1024 // 1024}MB ({total_saved // 1024}KB)")

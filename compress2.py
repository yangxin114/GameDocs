#!/usr/bin/env python3
"""Compress remaining large images to JPG at 85% quality and update HTML references."""
import os
from PIL import Image

BASE = r"C:\Users\Lewis\Desktop\GameDev\GamePrjs\DarkGame\dark-game"
MIN_SIZE = 200 * 1024  # 200KB
QUALITY = 85

converted = []

for root, dirs, files in os.walk(os.path.join(BASE, "assets", "images")):
    for f in files:
        if f.lower().endswith('.png') or f.lower().endswith('.jpg'):
            path = os.path.join(root, f)
            size = os.path.getsize(path)
            if size > MIN_SIZE:
                try:
                    img = Image.open(path)
                    if img.mode in ('RGBA', 'P', 'LA'):
                        img = img.convert('RGB')
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')
                    jpg_path = path.rsplit('.', 1)[0] + '.jpg'
                    img.save(jpg_path, 'JPEG', quality=QUALITY, optimize=True)
                    jpg_size = os.path.getsize(jpg_path)
                    saved = size - jpg_size
                    if saved <= 0:
                        os.remove(jpg_path)
                        continue
                    pct = (saved / size) * 100
                    converted.append((f, path, jpg_path, size, jpg_size, pct))
                    if f.lower().endswith('.png'):
                        os.remove(path)
                except Exception as e:
                    print(f"Error: {f}: {e}")

# Update HTML references
html_dirs = [os.path.join(BASE, d) for d in ['games/diablo4', 'games/lastepoch', 'games/diablo2', 'games/pathofexile', 'games/pathofexile2', '.']]
for old_name, old_path, new_path, old_size, new_size, pct in converted:
    old_ext = '.png' if old_name.lower().endswith('.png') else '.jpg'
    new_name = os.path.basename(new_path)
    for html_dir in html_dirs:
        if not os.path.isdir(html_dir):
            continue
        for html_file in os.listdir(html_dir):
            if not html_file.endswith('.html'):
                continue
            html_path = os.path.join(html_dir, html_file)
            try:
                with open(html_path, 'r', encoding='utf-8') as hf:
                    content = hf.read()
                if old_name in content:
                    content = content.replace(old_name, new_name)
                    with open(html_path, 'w', encoding='utf-8') as hf:
                        hf.write(content)
            except:
                pass

converted.sort(key=lambda x: x[3], reverse=True)

total_orig = sum(x[3] for x in converted)
total_new = sum(x[4] for x in converted)
print(f"Compressed {len(converted)} images")
print(f"Total: {total_orig/1024:.0f}KB -> {total_new/1024:.0f}KB (saved {(total_orig-total_new)/1024:.0f}KB, {(total_orig-total_new)/total_orig*100:.0f}%)")
for name, op, np, os2, ns, pct in converted:
    print(f"  {name}: {os2//1024}KB -> {ns//1024}KB ({pct:.0f}%)")

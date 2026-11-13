"""Convert rendered PNG frames to WebP for the home page.
python scripts/frames.py blender/out/hero_m public/hero/m [quality]
Writes 0000.webp ... and manifest.json {count, w, h}."""
import sys, os, json, glob
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
q = int(sys.argv[3]) if len(sys.argv) > 3 else 76
os.makedirs(dst, exist_ok=True)
files = sorted(glob.glob(os.path.join(src, 'f_*.png')))
# only a gap-free run from frame 0 is usable
run = []
for i, f in enumerate(files):
    if os.path.basename(f) != f'f_{i:04d}.png':
        break
    run.append(f)
total = 0
for i, f in enumerate(run):
    im = Image.open(f).convert('RGB')
    out = os.path.join(dst, f'{i:04d}.webp')
    im.save(out, 'WEBP', quality=q, method=6)
    total += os.path.getsize(out)
w, h = Image.open(run[0]).size if run else (0, 0)
json.dump({'count': len(run), 'w': w, 'h': h}, open(os.path.join(dst, 'manifest.json'), 'w'))
print(f'{len(run)} frames, {total // 1024} KB total, {w}x{h}')

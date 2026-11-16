"""Turn the generated clips into scroll frames for the landing page (v2: wide + tall film).

  .venv/bin/python scripts/clips_to_frames.py [fps] [quality]

Reads blender/out/media/v2/{wide,tall}/<A>-<B>.mp4 (see HIGGSFIELD-BRIEF-V2.md), writes
public/hero/{wide,tall}/<chapter>/NNNN.webp and public/hero/story.json:
  { wide: {w,h}, tall: {w,h},
    chapters: [ { id, count, stages: [frame index of each key image],
                  lum: { wide: "0-9 per frame", tall: "..." } } ] }
lum = brightness of the part of the frame where the text sits (left 40% wide, top 35% tall),
so the page knows when to switch to white text.
"""
import sys, os, json, glob, shutil, subprocess, tempfile
from PIL import Image, ImageStat
import imageio_ffmpeg

FPS = float(sys.argv[1]) if len(sys.argv) > 1 else 6
Q = int(sys.argv[2]) if len(sys.argv) > 2 else 62
SIZE = {'wide': (1024, 576), 'tall': (576, 1024)}
TEXT = {'wide': (0.0, 0.2, 0.4, 0.8), 'tall': (0.0, 0.08, 1.0, 0.36)}   # x0, y0, x1, y1 of the text area
SRC, DST = 'blender/out/media/v2', 'public/hero'
CHAPTERS = [
    ('torta', ['T1-T2', 'T2-T3', 'T3-T4']),
    ('pecivo', ['P1-P2', 'P2-P3', 'P3-P4']),
    ('jelo', ['M1-M2', 'M2-M3', 'M3-M4']),
]
ff = imageio_ffmpeg.get_ffmpeg_exe()
shutil.rmtree(DST, ignore_errors=True)
story = {**{k: {'w': v[0], 'h': v[1]} for k, v in SIZE.items()}, 'chapters': []}
for cid, clips in CHAPTERS:
    ch = {'id': cid, 'lum': {}}
    for fmt, (W, H) in SIZE.items():
        out = os.path.join(DST, fmt, cid)
        os.makedirs(out)
        n, stages, lum, size = 0, [0], '', 0
        for ci, clip in enumerate(clips):
            tmp = tempfile.mkdtemp()
            subprocess.run([ff, '-v', 'error', '-i', f'{SRC}/{fmt}/{clip}.mp4', '-vf', f'fps={FPS},scale={W}:{H}:flags=lanczos', f'{tmp}/%04d.png'], check=True)
            frames = sorted(glob.glob(f'{tmp}/*.png'))
            if ci:                      # the join frame is the same picture as the previous clip's last frame
                frames = frames[1:]
            for f in frames:
                im = Image.open(f).convert('RGB')
                p = f'{out}/{n:04d}.webp'
                im.save(p, 'WEBP', quality=Q, method=6)
                size += os.path.getsize(p)
                x0, y0, x1, y1 = TEXT[fmt]
                l = ImageStat.Stat(im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))).convert('L')).mean[0]
                lum += str(min(9, int(l / 25.6)))
                n += 1
            stages.append(n - 1)
            shutil.rmtree(tmp)
        assert ch.get('count', n) == n, 'wide and tall clips differ in length'
        ch.update(count=n, stages=stages)
        ch['lum'][fmt] = lum
        print(cid, fmt, n, 'frames, stages', stages, round(size / 1e6, 2), 'MB\n  ', lum)
    story['chapters'].append(ch)
json.dump(story, open(f'{DST}/story.json', 'w'))

"""Turn the generated clips into scroll frames for the landing page.

  .venv/bin/python scripts/clips_to_frames.py [fps] [quality]

Reads blender/out/media/<A>-<B>.mp4 (see HIGGSFIELD-BRIEF.md), writes
public/hero/<chapter>/NNNN.webp and public/hero/story.json:
  { w, h, chapters: [ { id, count, stages: [frame index where each key image sits] } ] }
"""
import sys, os, json, glob, shutil, subprocess, tempfile
from PIL import Image
import imageio_ffmpeg

FPS = float(sys.argv[1]) if len(sys.argv) > 1 else 6
Q = int(sys.argv[2]) if len(sys.argv) > 2 else 72
W, H = 540, 960
SRC, DST = 'blender/out/media', 'public/hero'
CHAPTERS = [
    ('torta', ['T1-T2', 'T2-T3', 'T3-T4', 'T4-T5']),
    ('pecivo', ['P1-P2', 'P2-P3', 'P3-P4']),
    ('jelo', ['M1-M2', 'M2-M3']),
]
ff = imageio_ffmpeg.get_ffmpeg_exe()
story = {'w': W, 'h': H, 'chapters': []}
total = 0
for cid, clips in CHAPTERS:
    out = os.path.join(DST, cid)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    n, stages = 0, [0]
    for ci, clip in enumerate(clips):
        tmp = tempfile.mkdtemp()
        subprocess.run([ff, '-v', 'error', '-i', f'{SRC}/{clip}.mp4', '-vf', f'fps={FPS},scale={W}:{H}:flags=lanczos', f'{tmp}/%04d.png'], check=True)
        frames = sorted(glob.glob(f'{tmp}/*.png'))
        if ci:                      # the join frame is the same picture as the previous clip's last frame
            frames = frames[1:]
        for f in frames:
            p = f'{out}/{n:04d}.webp'
            Image.open(f).convert('RGB').save(p, 'WEBP', quality=Q, method=6)
            total += os.path.getsize(p)
            n += 1
        stages.append(n - 1)
        shutil.rmtree(tmp)
    story['chapters'].append({'id': cid, 'count': n, 'stages': stages})
    print(cid, n, 'frames, stages at', stages)
json.dump(story, open(f'{DST}/story.json', 'w'))
print('total', round(total / 1e6, 2), 'MB')

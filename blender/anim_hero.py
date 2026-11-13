"""Station 0 -> 1: the logo objects roll and slide off the cloth.
Blender -b -P blender/anim_hero.py -- <out_dir> [pct] [samples] [frames]
Resumable: frames that already exist are skipped.
"""
import bpy, sys, os, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scene

argv = sys.argv[sys.argv.index('--') + 1:]
out = os.path.abspath(argv[0])
pct = int(argv[1]) if len(argv) > 1 else 50
samples = int(argv[2]) if len(argv) > 2 else 32
FRAMES = int(argv[3]) if len(argv) > 3 else 48
os.makedirs(out, exist_ok=True)

O = scene.build()
scene.render_settings(pct=pct, samples=samples)
sc = bpy.context.scene
sc.frame_start, sc.frame_end = 0, FRAMES - 1


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def key(o, f):
    o.keyframe_insert('location', frame=f)
    o.keyframe_insert('rotation_euler', frame=f)


HOLD = round(FRAMES * 0.12)          # logo rests for the first bit of scroll
start = {k: (O[k].location.copy(), O[k].rotation_euler.copy()) for k in ('pin', 'loaf_top', 'loaf_bottom', 'fork', 'knife')}
R = 14 * scene.U
fa, ka = math.radians(40), math.radians(138)
for f in range(FRAMES):
    t = ease((f - HOLD) / (FRAMES - 1 - HOLD))
    # rolling pin rolls off to the left (rotation matches the distance travelled)
    d = 0.62 * t
    loc, rot = start['pin']
    O['pin'].location = (loc.x - d, loc.y, loc.z)
    O['pin'].rotation_euler = (rot.x, rot.y - d / R, rot.z)
    key(O['pin'], f)
    # loaves are pushed apart, turning a little
    for k, dy, dx, tw in (('loaf_top', 0.62, -0.10, 0.5), ('loaf_bottom', -0.62, -0.06, -0.4)):
        loc, rot = start[k]
        tt = ease((f - HOLD - 3) / (FRAMES - 1 - HOLD - 3))
        O[k].location = (loc.x + dx * tt, loc.y + dy * tt, loc.z)
        O[k].rotation_euler = (rot.x, rot.y, rot.z + tw * tt)
        key(O[k], f)
    # fork and knife slide out along their own direction
    for k, a, lag in (('fork', fa, 1), ('knife', ka, 5)):
        loc, rot = start[k]
        tt = ease((f - HOLD - lag) / (FRAMES - 1 - HOLD - lag))
        O[k].location = (loc.x + math.sin(a) * 0.6 * tt, loc.y + math.cos(a) * 0.6 * tt, loc.z)
        O[k].rotation_euler = (rot.x, rot.y, rot.z - 0.35 * tt)
        key(O[k], f)

t0 = time.time()
for f in range(FRAMES):
    path = os.path.join(out, f'f_{f:04d}.png')
    if os.path.exists(path):
        continue
    sc.frame_set(f)
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print(f'FRAME {f + 1}/{FRAMES} {round(time.time() - t0)}s', flush=True)
print('ANIM_DONE', round(time.time() - t0), flush=True)

"""Render one test still.  Blender -b -P blender/still.py -- out.png [pct] [samples]"""
import bpy, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scene
argv = sys.argv[sys.argv.index('--') + 1:]
out, pct, samples = argv[0], int(argv[1]) if len(argv) > 1 else 50, int(argv[2]) if len(argv) > 2 else 48
scene.build()
scene.render_settings(pct=pct, samples=samples)
bpy.context.scene.render.filepath = os.path.abspath(out)
t = time.time()
bpy.ops.render.render(write_still=True)
print('RENDER_SECONDS', round(time.time() - t, 1))

import bpy, sys
bpy.ops.wm.read_factory_settings(use_empty=True)
for p in sys.argv[sys.argv.index('--') + 1:]:
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=p)
    for o in set(bpy.data.objects) - before:
        print('OBJ', p.split('/')[-1], o.name, o.type, [round(d, 3) for d in o.dimensions], [round(x, 3) for x in o.location], o.parent.name if o.parent else None)

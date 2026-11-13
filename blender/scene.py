"""Biljin sto — builds the top-down kitchen-table scene from scratch (no downloaded assets).

Run:  Blender -b -P blender/scene.py -- [--save out.blend]
Other scripts import build() from here.
Units: metres. Table top is z = 0. Camera looks straight down (-Z); +Y is "up" on screen.
"""
import bpy, bmesh, math, sys, random, os
from mathutils import Vector, Euler

U = 0.0022  # one logo (SVG) unit in metres
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')   # Poly Haven CC0 files (see ASSETS.md); optional
HAS_ASSETS = os.path.isdir(os.path.join(ASSETS, 'tex'))


def L(sx, sy):
    """logo SVG coords -> world XY (logo centre at 110,100)."""
    return ((sx - 110) * U, -(sy - 100) * U)


# ------------------------------------------------------------------ helpers
def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def mat(name):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    b = nt.nodes.new('ShaderNodeBsdfPrincipled')
    nt.links.new(b.outputs['BSDF'], out.inputs['Surface'])
    return m, nt, b, out


def N(nt, kind, **props):
    n = nt.nodes.new(kind)
    for k, v in props.items():
        setattr(n, k, v)
    return n


def ramp(nt, stops, interp='LINEAR'):
    r = N(nt, 'ShaderNodeValToRGB')
    r.color_ramp.interpolation = interp
    els = r.color_ramp.elements
    while len(els) > 1:
        els.remove(els[-1])
    els[0].position, els[0].color = stops[0][0], stops[0][1]
    for pos, col in stops[1:]:
        e = els.new(pos)
        e.color = col
    return r


def rgb(hexs, a=1.0):
    h = hexs.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(pow(x, 2.2) for x in c) + (a,)  # sRGB -> linear


def shade_smooth(o):
    for p in o.data.polygons:
        p.use_smooth = True


def add_mod(o, kind, name, **props):
    m = o.modifiers.new(name, kind)
    for k, v in props.items():
        setattr(m, k, v)
    return m


def link(o):
    bpy.context.scene.collection.objects.link(o)
    return o


def mesh_obj(name, bm):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return link(bpy.data.objects.new(name, me))


# ------------------------------------------------------------------ materials
def m_wood_table():
    m, nt, b, out = mat('TableOak')
    tc = N(nt, 'ShaderNodeTexCoord')
    mp = N(nt, 'ShaderNodeMapping')
    mp.inputs['Scale'].default_value = (1.0, 9.0, 1.0)       # stretch grain along X
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
    noise = N(nt, 'ShaderNodeTexNoise')
    noise.inputs['Scale'].default_value = 5.5
    noise.inputs['Detail'].default_value = 9
    noise.inputs['Roughness'].default_value = 0.62
    noise.inputs['Distortion'].default_value = 1.6
    nt.links.new(mp.outputs['Vector'], noise.inputs['Vector'])
    fine = N(nt, 'ShaderNodeTexNoise')
    fine.inputs['Scale'].default_value = 90
    fine.inputs['Detail'].default_value = 4
    nt.links.new(mp.outputs['Vector'], fine.inputs['Vector'])
    # planks: bricks along X
    brick = N(nt, 'ShaderNodeTexBrick')
    brick.offset = 0.37
    brick.inputs['Scale'].default_value = 1.0
    brick.inputs['Brick Width'].default_value = 1.9
    brick.inputs['Row Height'].default_value = 0.145
    brick.inputs['Mortar Size'].default_value = 0.0016
    brick.inputs['Mortar Smooth'].default_value = 0.6
    brick.inputs['Color1'].default_value = (0.42, 0.42, 0.42, 1)
    brick.inputs['Color2'].default_value = (0.62, 0.62, 0.62, 1)
    brick.inputs['Mortar'].default_value = (0, 0, 0, 1)
    nt.links.new(tc.outputs['Object'], brick.inputs['Vector'])
    cr = ramp(nt, [(0.28, rgb('#6E4A2C')), (0.5, rgb('#9A6C40')), (0.72, rgb('#B98A56'))])
    nt.links.new(noise.outputs['Fac'], cr.inputs['Fac'])
    mixp = N(nt, 'ShaderNodeMixRGB', blend_type='MULTIPLY')
    mixp.inputs['Fac'].default_value = 0.55
    nt.links.new(cr.outputs['Color'], mixp.inputs['Color1'])
    nt.links.new(brick.outputs['Color'], mixp.inputs['Color2'])
    # brighten a touch after the multiply
    hsv = N(nt, 'ShaderNodeHueSaturation')
    hsv.inputs['Value'].default_value = 1.75
    hsv.inputs['Saturation'].default_value = 0.92
    nt.links.new(mixp.outputs['Color'], hsv.inputs['Color'])
    nt.links.new(hsv.outputs['Color'], b.inputs['Base Color'])
    rr = ramp(nt, [(0.3, (0.38,) * 3 + (1,)), (0.8, (0.58,) * 3 + (1,))])
    nt.links.new(fine.outputs['Fac'], rr.inputs['Fac'])
    nt.links.new(rr.outputs['Color'], b.inputs['Roughness'])
    bump = N(nt, 'ShaderNodeBump')
    bump.inputs['Strength'].default_value = 0.22
    bump.inputs['Distance'].default_value = 0.002
    addh = N(nt, 'ShaderNodeMath', operation='ADD')
    nt.links.new(noise.outputs['Fac'], addh.inputs[0])
    nt.links.new(brick.outputs['Fac'], addh.inputs[1])
    nt.links.new(addh.outputs[0], bump.inputs['Height'])
    nt.links.new(bump.outputs['Normal'], b.inputs['Normal'])
    return m


def m_linen():
    m, nt, b, out = mat('Linen')
    tc = N(nt, 'ShaderNodeTexCoord')
    sep = N(nt, 'ShaderNodeSeparateXYZ')
    nt.links.new(tc.outputs['Object'], sep.inputs[0])
    # woven threads: two sine waves, warp and weft
    def wave(axis):
        mul = N(nt, 'ShaderNodeMath', operation='MULTIPLY')
        mul.inputs[1].default_value = 2600.0
        nt.links.new(sep.outputs[axis], mul.inputs[0])
        s = N(nt, 'ShaderNodeMath', operation='SINE')
        nt.links.new(mul.outputs[0], s.inputs[0])
        return s
    wx, wy = wave('X'), wave('Y')
    mx = N(nt, 'ShaderNodeMath', operation='MULTIPLY')
    nt.links.new(wx.outputs[0], mx.inputs[0])
    nt.links.new(wy.outputs[0], mx.inputs[1])
    slub = N(nt, 'ShaderNodeTexNoise')
    slub.inputs['Scale'].default_value = 60
    slub.inputs['Detail'].default_value = 6
    mp = N(nt, 'ShaderNodeMapping')
    mp.inputs['Scale'].default_value = (1, 14, 1)
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
    nt.links.new(mp.outputs['Vector'], slub.inputs['Vector'])
    cr = ramp(nt, [(0.3, rgb('#BFB094')), (0.7, rgb('#DDD0B6'))])
    nt.links.new(slub.outputs['Fac'], cr.inputs['Fac'])
    nt.links.new(cr.outputs['Color'], b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = 0.92
    b.inputs['Sheen Weight'].default_value = 0.35
    bump = N(nt, 'ShaderNodeBump')
    bump.inputs['Strength'].default_value = 0.5
    bump.inputs['Distance'].default_value = 0.0006
    ad = N(nt, 'ShaderNodeMath', operation='ADD')
    nt.links.new(mx.outputs[0], ad.inputs[0])
    nt.links.new(slub.outputs['Fac'], ad.inputs[1])
    nt.links.new(ad.outputs[0], bump.inputs['Height'])
    nt.links.new(bump.outputs['Normal'], b.inputs['Normal'])
    return m


def m_bread():
    m, nt, b, out = mat('BreadCrust')
    tc = N(nt, 'ShaderNodeTexCoord')
    geo = N(nt, 'ShaderNodeNewGeometry')
    big = N(nt, 'ShaderNodeTexNoise')
    big.inputs['Scale'].default_value = 9
    big.inputs['Detail'].default_value = 8
    big.inputs['Roughness'].default_value = 0.6
    nt.links.new(tc.outputs['Object'], big.inputs['Vector'])
    # darker on top (more baked), paler near the base
    sepn = N(nt, 'ShaderNodeSeparateXYZ')
    nt.links.new(geo.outputs['Normal'], sepn.inputs[0])
    ad = N(nt, 'ShaderNodeMath', operation='MULTIPLY_ADD')
    ad.inputs[1].default_value = 0.55
    nt.links.new(sepn.outputs['Z'], ad.inputs[0])
    nt.links.new(big.outputs['Fac'], ad.inputs[2])
    cr = ramp(nt, [(0.3, rgb('#E6BC78')), (0.58, rgb('#CC8F4A')), (0.84, rgb('#A0602A')), (1.0, rgb('#74401A'))])
    nt.links.new(ad.outputs[0], cr.inputs['Fac'])
    # flour dusting: white patches, mostly on top
    fl = N(nt, 'ShaderNodeTexNoise')
    fl.inputs['Scale'].default_value = 26
    fl.inputs['Detail'].default_value = 10
    fl.inputs['Roughness'].default_value = 0.75
    nt.links.new(tc.outputs['Object'], fl.inputs['Vector'])
    fm = N(nt, 'ShaderNodeMath', operation='MULTIPLY')
    nt.links.new(fl.outputs['Fac'], fm.inputs[0])
    nt.links.new(sepn.outputs['Z'], fm.inputs[1])
    fr = ramp(nt, [(0.5, (0, 0, 0, 1)), (0.72, (0.8, 0.8, 0.8, 1))])
    nt.links.new(fm.outputs[0], fr.inputs['Fac'])
    mixf = N(nt, 'ShaderNodeMixRGB')
    nt.links.new(fr.outputs['Color'], mixf.inputs['Fac'])
    nt.links.new(cr.outputs['Color'], mixf.inputs['Color1'])
    mixf.inputs['Color2'].default_value = rgb('#F4EEE2')
    nt.links.new(mixf.outputs['Color'], b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = 0.78
    b.inputs['Subsurface Weight'].default_value = 0.12
    b.inputs['Subsurface Radius'].default_value = (0.012, 0.006, 0.003)
    # crackly crust
    cells = N(nt, 'ShaderNodeTexVoronoi', feature='DISTANCE_TO_EDGE')
    cells.inputs['Scale'].default_value = 34
    nt.links.new(tc.outputs['Object'], cells.inputs['Vector'])
    fine = N(nt, 'ShaderNodeTexNoise')
    fine.inputs['Scale'].default_value = 160
    fine.inputs['Detail'].default_value = 5
    nt.links.new(tc.outputs['Object'], fine.inputs['Vector'])
    hh = N(nt, 'ShaderNodeMath', operation='ADD')
    nt.links.new(cells.outputs['Distance'], hh.inputs[0])
    nt.links.new(fine.outputs['Fac'], hh.inputs[1])
    bump = N(nt, 'ShaderNodeBump')
    bump.inputs['Strength'].default_value = 0.28
    bump.inputs['Distance'].default_value = 0.0018
    nt.links.new(hh.outputs[0], bump.inputs['Height'])
    nt.links.new(bump.outputs['Normal'], b.inputs['Normal'])
    return m


def m_crumb():
    m, nt, b, out = mat('BreadScore')
    b.inputs['Base Color'].default_value = rgb('#F0D9AE')
    b.inputs['Roughness'].default_value = 0.9
    b.inputs['Subsurface Weight'].default_value = 0.2
    return m


def m_pinwood():
    m, nt, b, out = mat('BeechPin')
    tc = N(nt, 'ShaderNodeTexCoord')
    mp = N(nt, 'ShaderNodeMapping')
    mp.inputs['Scale'].default_value = (14, 1.2, 14)
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
    n = N(nt, 'ShaderNodeTexNoise')
    n.inputs['Scale'].default_value = 7
    n.inputs['Detail'].default_value = 8
    n.inputs['Distortion'].default_value = 0.8
    nt.links.new(mp.outputs['Vector'], n.inputs['Vector'])
    cr = ramp(nt, [(0.3, rgb('#C99A5E')), (0.6, rgb('#E2BD86')), (0.85, rgb('#EFD4A6'))])
    nt.links.new(n.outputs['Fac'], cr.inputs['Fac'])
    nt.links.new(cr.outputs['Color'], b.inputs['Base Color'])
    b.inputs['Roughness'].default_value = 0.42
    b.inputs['Coat Weight'].default_value = 0.15
    bump = N(nt, 'ShaderNodeBump')
    bump.inputs['Strength'].default_value = 0.08
    nt.links.new(n.outputs['Fac'], bump.inputs['Height'])
    nt.links.new(bump.outputs['Normal'], b.inputs['Normal'])
    return m


def m_steel():
    m, nt, b, out = mat('Steel')
    b.inputs['Base Color'].default_value = (0.72, 0.72, 0.73, 1)
    b.inputs['Metallic'].default_value = 1.0
    tc = N(nt, 'ShaderNodeTexCoord')
    mp = N(nt, 'ShaderNodeMapping')
    mp.inputs['Scale'].default_value = (400, 3, 400)   # brushed along the length
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
    n = N(nt, 'ShaderNodeTexNoise')
    n.inputs['Scale'].default_value = 3
    n.inputs['Detail'].default_value = 3
    nt.links.new(mp.outputs['Vector'], n.inputs['Vector'])
    rr = ramp(nt, [(0.3, (0.16,) * 3 + (1,)), (0.75, (0.34,) * 3 + (1,))])
    nt.links.new(n.outputs['Fac'], rr.inputs['Fac'])
    nt.links.new(rr.outputs['Color'], b.inputs['Roughness'])
    return m


def m_handle():
    m, nt, b, out = mat('KnifeHandle')
    b.inputs['Base Color'].default_value = rgb('#7A3E22')
    b.inputs['Roughness'].default_value = 0.38
    b.inputs['Coat Weight'].default_value = 0.3
    return m


def m_flour():
    m, nt, b, out = mat('Flour')
    b.inputs['Base Color'].default_value = rgb('#F6F1E7')
    b.inputs['Roughness'].default_value = 1.0
    b.inputs['Subsurface Weight'].default_value = 0.3
    return m



# ------------------------------------------------------------------ scanned (Poly Haven, CC0) materials and models
def m_scan(name, tid, scale=(1, 1, 1), rot=0.0, bump=1.0, value=1.0, sheen=0.0):
    """Principled material from a Poly Haven texture set (diff / rough / nor_gl)."""
    m, nt, b, out = mat(name)
    tc = N(nt, 'ShaderNodeTexCoord')
    mp = N(nt, 'ShaderNodeMapping')
    mp.inputs['Scale'].default_value = scale
    mp.inputs['Rotation'].default_value = (0, 0, rot)
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])

    def img(short, data=False):
        n = N(nt, 'ShaderNodeTexImage')
        n.image = bpy.data.images.load(os.path.join(ASSETS, 'tex', f'{tid}_{short}.jpg'), check_existing=True)
        if data:
            n.image.colorspace_settings.name = 'Non-Color'
        nt.links.new(mp.outputs['Vector'], n.inputs['Vector'])
        return n
    d = img('diff')
    hsv = N(nt, 'ShaderNodeHueSaturation')
    hsv.inputs['Value'].default_value = value
    nt.links.new(d.outputs['Color'], hsv.inputs['Color'])
    nt.links.new(hsv.outputs['Color'], b.inputs['Base Color'])
    nt.links.new(img('rough', True).outputs['Color'], b.inputs['Roughness'])
    nm = N(nt, 'ShaderNodeNormalMap')
    nm.inputs['Strength'].default_value = bump
    nt.links.new(img('nor', True).outputs['Color'], nm.inputs['Color'])
    nt.links.new(nm.outputs['Normal'], b.inputs['Normal'])
    b.inputs['Sheen Weight'].default_value = sheen
    return m


def import_gltf(folder, name):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, folder, f'{folder}_1k.gltf'))
    new = sorted(set(bpy.data.objects) - before, key=lambda o: o.name)
    return [o for o in new if o.type == 'MESH']


def make_bun_loaf(src, name, cx, cy, sx, sy, sz, rot):
    """A scanned bun stretched into a small oval loaf."""
    o = src
    o.name = name
    o.parent = None
    bpy.context.view_layer.update()
    # put the origin at the middle of the base so it sits on the table
    bb = [Vector(c) for c in o.bound_box]
    cxl = sum(v.x for v in bb) / 8
    cyl = sum(v.y for v in bb) / 8
    zmin = min(v.z for v in bb)
    for v in o.data.vertices:
        v.co.x -= cxl
        v.co.y -= cyl
        v.co.z -= zmin
    o.rotation_mode = 'XYZ'
    o.location = (cx, cy, 0.003)
    o.rotation_euler = (0, 0, rot)
    o.scale = (sx, sy, sz)
    return o


def world_hdri(strength=0.45, rot=0.0):
    w = bpy.context.scene.world
    nt = w.node_tree
    bg = nt.nodes['Background']
    tc = nt.nodes.new('ShaderNodeTexCoord')
    mp = nt.nodes.new('ShaderNodeMapping')
    mp.inputs['Rotation'].default_value = (0, 0, rot)
    env = nt.nodes.new('ShaderNodeTexEnvironment')
    env.image = bpy.data.images.load(os.path.join(ASSETS, 'hdri', 'comfy_cafe_1k.hdr'), check_existing=True)
    nt.links.new(tc.outputs['Generated'], mp.inputs['Vector'])
    nt.links.new(mp.outputs['Vector'], env.inputs['Vector'])
    nt.links.new(env.outputs['Color'], bg.inputs['Color'])
    bg.inputs['Strength'].default_value = strength

# ------------------------------------------------------------------ objects
def make_table(M):
    bpy.ops.mesh.primitive_plane_add(size=1)
    o = bpy.context.object
    o.name = 'Table'
    o.scale = (2.2, 6.0, 1)
    o.location = (0, -1.6, 0)
    o.data.materials.append(M['table'])
    return o


def make_cloth(M, center=(0.0, 0.0), size=(0.66, 0.86), rot=math.radians(-4)):
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=90, y_segments=110, size=0.5)
    o = mesh_obj('LinenCloth', bm)
    o.scale = (size[0], size[1], 1)
    o.location = (center[0], center[1], 0.0015)
    o.rotation_euler = (0, 0, rot)
    tex = bpy.data.textures.new('ClothWrinkle', 'CLOUDS')
    tex.noise_scale = 0.22
    tex.noise_depth = 2
    add_mod(o, 'DISPLACE', 'Wrinkle', texture=tex, strength=0.006, mid_level=0.35, texture_coords='GLOBAL')
    add_mod(o, 'SOLIDIFY', 'Thick', thickness=0.0012)
    shade_smooth(o)
    o.data.materials.append(M['linen'])
    return o


def make_loaf(M, name, cx, cy, rx, ry, h, seed=0, slashes=3, rot=0.0):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=64, v_segments=40, radius=1.0)
    # flatten the underside so it sits on the table
    for v in bm.verts:
        if v.co.z < -0.25:
            v.co.z = -0.25 - (v.co.z + 0.25) * 0.12
    o = mesh_obj(name, bm)
    o.scale = (rx, ry, h)
    o.location = (cx, cy, h * 0.26)
    o.rotation_euler = (0, 0, rot)
    tex = bpy.data.textures.new(name + 'Lump', 'CLOUDS')
    tex.noise_scale = 0.9 + seed * 0.13
    tex.noise_depth = 3
    add_mod(o, 'DISPLACE', 'Lumps', texture=tex, strength=0.12, mid_level=0.5, texture_coords='LOCAL')
    add_mod(o, 'SUBSURF', 'Smooth', levels=1, render_levels=2)
    shade_smooth(o)
    o.data.materials.append(M['bread'])
    # scoring: pale diagonal cuts lying on the crust
    for i in range(slashes):
        t = (i - (slashes - 1) / 2) * 0.42
        bm2 = bmesh.new()
        bmesh.ops.create_uvsphere(bm2, u_segments=24, v_segments=12, radius=1.0)
        s = mesh_obj(f'{name}Score{i}', bm2)
        s.scale = (rx * 0.42, ry * 0.045, h * 0.10)
        s.rotation_euler = (0, 0, rot + math.radians(38))
        ox, oy = math.cos(rot + math.radians(128)) * t * ry * 0.9, math.sin(rot + math.radians(128)) * t * ry * 0.9
        zz = h * 0.26 + h * math.sqrt(max(0.05, 1 - (t * 0.9) ** 2)) * 0.97
        s.location = (cx + ox, cy + oy, zz)
        shade_smooth(s)
        s.data.materials.append(M['crumb'])
        s.parent = o
        s.matrix_parent_inverse = o.matrix_world.inverted()
    return o


def make_pin(M, cx, cy, body_len, r, handle_len, handle_r):
    def cyl(name, length, radius, y):
        bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=radius, depth=length, location=(cx, cy + y, r), rotation=(math.pi / 2, 0, 0))
        o = bpy.context.object
        o.name = name
        add_mod(o, 'BEVEL', 'Edge', width=radius * 0.32, segments=6, limit_method='ANGLE')
        shade_smooth(o)
        o.data.materials.append(M['pin'])
        return o
    body = cyl('RollingPin', body_len, r, 0)
    for sgn in (1, -1):
        h = cyl('PinHandle', handle_len, handle_r, sgn * (body_len / 2 + handle_len / 2 - 0.004))
        h.parent = body
        h.matrix_parent_inverse = body.matrix_world.inverted()
        bpy.ops.mesh.primitive_uv_sphere_add(radius=handle_r * 1.25, segments=32, ring_count=16, location=(cx, cy + sgn * (body_len / 2 + handle_len - 0.004), r))
        k = bpy.context.object
        k.name = 'PinKnob'
        k.scale = (1, 0.8, 1)
        shade_smooth(k)
        k.data.materials.append(M['pin'])
        k.parent = body
        k.matrix_parent_inverse = body.matrix_world.inverted()
    return body


def box(name, sx, sy, sz, loc, mat_, bevel=0.0008, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = (sx, sy, sz)
    add_mod(o, 'BEVEL', 'Edge', width=bevel, segments=3)
    shade_smooth(o)
    o.data.materials.append(mat_)
    if parent:
        o.parent = parent
    return o


def make_fork(M, x, y, ang):
    """Fork lying flat. Local +Y is from handle end to tines. ang = direction of +Y on the table (radians, 0 = +Y, clockwise positive)."""
    root = bpy.data.objects.new('Fork', None)
    link(root)
    z = 0.0022
    box('ForkHandle', 0.011, 0.118, 0.0032, (0, 0.059, z), M['steel'], 0.0012, root)
    box('ForkNeck', 0.0075, 0.03, 0.0028, (0, 0.13, z), M['steel'], 0.001, root)
    box('ForkBase', 0.026, 0.02, 0.0024, (0, 0.152, z), M['steel'], 0.001, root)
    for i in range(4):
        box(f'ForkTine{i}', 0.0042, 0.05, 0.0020, (-0.0109 + i * 0.00727, 0.184, z), M['steel'], 0.0008, root)
    root.location = (x, y, 0.004)
    root.rotation_euler = (0, 0, -ang)
    root.scale = (1.3, 1.12, 1.3)
    return root


def make_knife(M, x, y, ang):
    root = bpy.data.objects.new('Knife', None)
    link(root)
    box('KnifeHandle', 0.019, 0.105, 0.011, (0, 0.0525, 0.0055), M['handle'], 0.004, root)
    for yy in (0.03, 0.075):
        bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.0022, depth=0.0114, location=(0, yy, 0.0056))
        r = bpy.context.object
        r.name = 'KnifeRivet'
        r.data.materials.append(M['steel'])
        r.parent = root
    # blade outline (top view), then extrude thin
    pts = [(-0.0085, 0.103), (-0.0085, 0.215), (-0.0075, 0.238), (-0.0035, 0.253), (0.0045, 0.26), (0.0105, 0.255), (0.012, 0.18), (0.0098, 0.103)]
    bm = bmesh.new()
    vs = [bm.verts.new((px, py, 0.0)) for px, py in pts]
    f = bm.faces.new(vs)
    ext = bmesh.ops.extrude_face_region(bm, geom=[f])
    bmesh.ops.translate(bm, vec=(0, 0, 0.0018), verts=[v for v in ext['geom'] if isinstance(v, bmesh.types.BMVert)])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    blade = mesh_obj('KnifeBlade', bm)
    blade.location = (0, 0, 0.0046)
    add_mod(blade, 'BEVEL', 'Edge', width=0.0006, segments=2)
    blade.data.materials.append(M['steel'])
    blade.parent = root
    root.location = (x, y, 0.004)
    root.rotation_euler = (0, 0, -ang)
    return root


def make_flour(M, around, count=2600, seed=3):
    """Loose flour: tiny grains scattered on the cloth (one mesh, cheap to render)."""
    rnd = random.Random(seed)
    bm = bmesh.new()
    for _ in range(count):
        cx, cy, spread = rnd.choice(around)
        a, d = rnd.uniform(0, math.tau), abs(rnd.gauss(0, spread))
        s = rnd.uniform(0.0004, 0.0016)
        mtx = Euler((rnd.random() * 3, rnd.random() * 3, 0)).to_matrix().to_4x4()
        mtx.translation = Vector((cx + math.cos(a) * d, cy + math.sin(a) * d, 0.0034 + s * 0.4))
        bmesh.ops.create_icosphere(bm, subdivisions=1, radius=s, matrix=mtx)
    o = mesh_obj('FlourGrains', bm)
    o.data.materials.append(M['flour'])
    return o


# ------------------------------------------------------------------ light, camera, render
def make_light():
    w = bpy.data.worlds.new('World')
    bpy.context.scene.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes['Background']
    bg.inputs['Color'].default_value = (0.86, 0.90, 1.0, 1)   # cool sky fill
    bg.inputs['Strength'].default_value = 0.22
    # big soft "window" from the upper left, warm
    ld = bpy.data.lights.new('Window', 'AREA')
    ld.shape = 'RECTANGLE'
    ld.size, ld.size_y = 1.3, 0.9
    ld.energy = 150
    ld.color = (1.0, 0.93, 0.82)
    lo = link(bpy.data.objects.new('Window', ld))
    lo.location = (-1.15, 0.75, 0.95)
    lo.rotation_euler = Vector((0, 0, -1)).rotation_difference(Vector((1.15, -0.75, -0.95)).normalized()).to_euler()
    # weak bounce from the right so shadows are not black
    fd = bpy.data.lights.new('Bounce', 'AREA')
    fd.size = 1.6
    fd.energy = 18
    fd.color = (1.0, 0.96, 0.9)
    fo = link(bpy.data.objects.new('Bounce', fd))
    fo.location = (1.3, -0.5, 0.8)
    fo.rotation_euler = Vector((0, 0, -1)).rotation_difference(Vector((-1.3, 0.5, -0.8)).normalized()).to_euler()


def make_camera(portrait=True):
    cd = bpy.data.cameras.new('Cam')
    cd.lens = 50
    cd.sensor_fit = 'VERTICAL' if portrait else 'HORIZONTAL'
    co = link(bpy.data.objects.new('Cam', cd))
    co.location = (0.0, 0.0, 1.62)
    co.rotation_euler = (0, 0, 0)        # looks straight down
    cd.dof.use_dof = True
    cd.dof.focus_distance = 1.59
    cd.dof.aperture_fstop = 5.6
    bpy.context.scene.camera = co
    return co


def render_settings(w=1080, h=1920, samples=64, pct=100):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.device = 'CPU'
    sc.cycles.samples = samples
    sc.cycles.use_adaptive_sampling = True
    sc.cycles.adaptive_threshold = 0.03
    sc.cycles.use_denoising = True
    sc.cycles.max_bounces = 6
    sc.cycles.caustics_reflective = False
    sc.cycles.caustics_refractive = False
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = w, h, pct
    sc.render.use_persistent_data = True
    sc.view_settings.view_transform = 'AgX'
    try:
        sc.view_settings.look = 'AgX - Medium High Contrast'
    except Exception:
        pass
    sc.render.image_settings.file_format = 'PNG'


# ------------------------------------------------------------------ build
def build(use_assets=True):
    reset()
    scans = use_assets and HAS_ASSETS
    M = dict(table=m_wood_table(), linen=m_linen(), bread=m_bread(), crumb=m_crumb(), pin=m_pinwood(),
             steel=m_steel(), handle=m_handle(), flour=m_flour())
    if scans:
        M['table'] = m_scan('TablePlanks', 'brown_planks_09', scale=(0.55, 0.55, 0.55), rot=math.pi / 2, bump=1.2, value=1.15)
        M['linen'] = m_scan('RoughLinen', 'rough_linen', scale=(3.2, 3.2, 3.2), bump=1.6, value=1.25, sheen=0.3)
    O = {}
    O['table'] = make_table(M)
    O['cloth'] = make_cloth(M, center=(0.0, 0.0), size=(0.56, 0.74))
    # --- the logo, in real objects (positions taken from the SVG) ---
    px, py = L(38, 100)
    O['pin'] = make_pin(M, px, py, body_len=140 * U, r=14 * U, handle_len=17 * U, handle_r=6.5 * U)
    ux, uy = L(80, 65)
    lx, ly = L(86, 137)
    if scans:
        buns = import_gltf('hamburger_buns', 'bun')
        O['loaf_top'] = make_bun_loaf(buns[0], 'LoafTop', ux, uy, 1.22, 1.38, 1.0, math.radians(12))
        O['loaf_bottom'] = make_bun_loaf(buns[1], 'LoafBottom', lx, ly, 1.3, 1.5, 1.05, math.radians(200))
        for extra in buns[2:]:
            bpy.data.objects.remove(extra)
    else:
        O['loaf_top'] = make_loaf(M, 'LoafTop', ux, uy, rx=30 * U, ry=37 * U, h=0.05, seed=1, rot=math.radians(4))
        O['loaf_bottom'] = make_loaf(M, 'LoafBottom', lx, ly, rx=35 * U, ry=37 * U, h=0.055, seed=2, rot=math.radians(-5))
    fx, fy = L(108, 96)
    kx, ky = L(110, 106)
    O['fork'] = make_fork(M, fx, fy, math.radians(40))
    O['knife'] = make_knife(M, kx, ky, math.radians(138))
    O['flour'] = make_flour(M, [(ux, uy, 0.07), (lx, ly, 0.08), (px, py, 0.05), (0.12, -0.02, 0.1)])
    make_light()
    if scans:
        world_hdri()
    O['cam'] = make_camera()
    render_settings()
    return O


if __name__ == '__main__':
    argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
    build()
    if '--save' in argv:
        bpy.ops.wm.save_as_mainfile(filepath=argv[argv.index('--save') + 1])

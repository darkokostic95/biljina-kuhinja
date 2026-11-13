# Blender assets (not in git)

All from **Poly Haven** (https://polyhaven.com), licence **CC0** (free for any use, no attribution needed). Downloaded 2026-11-13 into `blender/assets/` (36 MB, ignored by git). Without this folder `scene.py` falls back to procedural materials and loaves.

| File | Used for |
|---|---|
| models `hamburger_buns` (1k glTF) | the two small loaves in the logo (stretched to ovals) |
| models `croissant`, `wooden_cutting_board` (1k glTF) | later stations (peciva, slano) |
| textures `brown_planks_09` (2k) | table top |
| textures `rough_linen` (2k) | linen cloth |
| textures `oak_veneer_01` (2k) | spare wood |
| HDRI `comfy_cafe` (1k) | room light and reflections |

Poly Haven has no scanned bread loaf, rolling pin, fork or table knife, so those stay modelled by `scene.py`.
To fetch again: models via `https://api.polyhaven.com/files/<id>` → `gltf.1k`, textures → `Diffuse/Rough/nor_gl` `2k.jpg`, HDRI → `hdri.1k.hdr`.

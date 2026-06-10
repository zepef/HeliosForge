"""
HeliosForge — Star Lifting Nozzle v0 Concept Design
Design Specification: DS-002

Status: READY FOR BLENDER MCP EXECUTION
Blocker: Blender MCP server not detected in Paperclip agent runtime at Phase 0 bootstrap.
         Execute this script manually in Blender or via Blender MCP when server is configured.

Scale note: All dimensions in Blender units. 1 unit = 1,000 km for this design (solar scale).
Real dimensions annotated in comments.

Author: StellarEngineer / LiftingSpecialist
Date: 2026-06-10
Phase: 0 (Bootstrap)
"""

import bpy
import math

def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def create_star_lifting_nozzle():
    """
    Star lifting nozzle assembly.
    Components:
      - Magnetic funnel (toroidal coil ring)
      - MHD acceleration throat (cylinder)
      - Exit nozzle (cone frustum)
      - Magnetic field lines (curved tubes, 8x)
      - Collection ring (torus at top)
    """
    clear_scene()

    # Materials
    mat_coil = bpy.data.materials.new("Mat_SuperconductingCoil")
    mat_coil.diffuse_color = (0.8, 0.5, 0.1, 1.0)  # copper/gold
    mat_coil.metallic = 0.95
    mat_coil.roughness = 0.1

    mat_throat = bpy.data.materials.new("Mat_TungstenThroat")
    mat_throat.diffuse_color = (0.6, 0.6, 0.65, 1.0)  # silver-grey W-Re
    mat_throat.metallic = 0.9

    mat_fieldline = bpy.data.materials.new("Mat_MagneticFieldLine")
    mat_fieldline.diffuse_color = (0.2, 0.3, 0.9, 0.7)
    mat_fieldline.use_nodes = True

    mat_collection = bpy.data.materials.new("Mat_CollectionRing")
    mat_collection.diffuse_color = (0.3, 0.7, 0.3, 1.0)  # green — active receiver
    mat_collection.metallic = 0.5

    # -- Magnetic funnel (toroidal superconducting coil) --
    # Real: major radius ~10,000 km, minor radius ~1,000 km
    # Scaled: major radius 10 units, minor radius 1 unit
    bpy.ops.mesh.primitive_torus_add(
        major_radius=10, minor_radius=1,
        major_segments=48, minor_segments=16,
        location=(0, 0, 0)
    )
    funnel_coil = bpy.context.active_object
    funnel_coil.name = "MagneticFunnel_ToroidalCoil"
    funnel_coil.data.materials.append(mat_coil)

    # -- MHD acceleration throat (cylinder) --
    # Real: 5,000 km radius, 20,000 km length
    # Scaled: 5 units radius, 20 units length
    bpy.ops.mesh.primitive_cylinder_add(
        radius=5, depth=20,
        location=(0, 0, 10),
        rotation=(0, 0, 0)
    )
    throat = bpy.context.active_object
    throat.name = "MHD_AccelerationThroat"
    throat.data.materials.append(mat_throat)

    # -- Exit nozzle (cone frustum) --
    # Real: small radius 5,000 km, large radius 15,000 km, length 30,000 km
    bpy.ops.mesh.primitive_cone_add(
        vertices=32,
        radius1=7.5,  # exit (wider)
        radius2=5,    # throat connection
        depth=15,
        location=(0, 0, 27.5)
    )
    exit_nozzle = bpy.context.active_object
    exit_nozzle.name = "ExitNozzle_Cone"
    exit_nozzle.data.materials.append(mat_throat)

    # -- Collection ring at top --
    # Real: ~50,000 km altitude above solar pole, torus captures ejected plasma
    bpy.ops.mesh.primitive_torus_add(
        major_radius=12, minor_radius=0.8,
        location=(0, 0, 45)
    )
    collection_ring = bpy.context.active_object
    collection_ring.name = "CollectionRing"
    collection_ring.data.materials.append(mat_collection)

    # -- Magnetic field lines (8 curved tubes approximated as bezier → mesh) --
    for i in range(8):
        angle = math.radians(i * 45)
        x_start = 10 * math.cos(angle)
        y_start = 10 * math.sin(angle)

        bpy.ops.curve.primitive_bezier_curve_add(location=(x_start, y_start, 0))
        curve = bpy.context.active_object
        curve.name = f"FieldLine_{i}"
        curve.data.bevel_depth = 0.15
        curve.data.bevel_resolution = 4

        # Adjust control points: start at funnel, arc to nozzle exit
        spline = curve.data.splines[0]
        spline.bezier_points[0].co = (x_start, y_start, 0)
        spline.bezier_points[0].handle_right = (x_start * 0.5, y_start * 0.5, 10)
        spline.bezier_points[1].co = (0, 0, 45)
        spline.bezier_points[1].handle_left = (x_start * 0.3, y_start * 0.3, 35)

        # Convert to mesh and apply material
        bpy.ops.object.convert(target='MESH')
        field_mesh = bpy.context.active_object
        field_mesh.data.materials.append(mat_fieldline)

    print("Star Lifting Nozzle geometry created.")
    print("Components: Toroidal coil, MHD throat, exit nozzle, collection ring, 8 field lines")
    print("Scale: 1 Blender unit = 1,000 km")


def export_stl(filepath="//star-lifting-nozzle-v0.stl"):
    bpy.ops.export_mesh.stl(filepath=filepath, use_selection=False)
    print(f"Exported STL: {filepath}")


def export_gltf(filepath="//star-lifting-nozzle-v0.gltf"):
    bpy.ops.export_scene.gltf(filepath=filepath, export_format='GLTF_EMBEDDED')
    print(f"Exported glTF: {filepath}")


if __name__ == "__main__":
    create_star_lifting_nozzle()
    export_stl()
    export_gltf()

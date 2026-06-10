"""
HeliosForge — Dyson Swarm Element v0 Concept Design
Design Specification: DS-001

Status: READY FOR BLENDER MCP EXECUTION
Blocker: Blender MCP server not detected in Paperclip agent runtime at Phase 0 bootstrap.
         Execute this script manually in Blender or via Blender MCP when server is configured.

Author: StellarEngineer / StellarArchitect
Date: 2026-06-10
Phase: 0 (Bootstrap)
"""

import bpy
import math

def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def create_dyson_swarm_element():
    """
    Hexagonal photovoltaic swarm element.
    Geometry: 10m flat-to-flat hexagon, 5mm structural depth.
    Scale: 1 Blender unit = 1 meter.
    """
    clear_scene()

    # -- Central hub --
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.25, depth=0.1, location=(0, 0, 0)
    )
    hub = bpy.context.active_object
    hub.name = "Hub_Central"

    # -- Hexagonal panel base (approximate via subdivided plane + radial trim) --
    # Use a circle with 6 vertices to define hex boundary
    bpy.ops.mesh.primitive_circle_add(
        vertices=6, radius=5.774, fill_type='NGON', location=(0, 0, 0)
    )
    hex_face = bpy.context.active_object
    hex_face.name = "Panel_PV_HexBase"

    # Extrude to give thickness
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.005)})
    bpy.ops.object.editmode_toggle()

    # Apply PV cell material
    mat_pv = bpy.data.materials.new(name="Mat_SolarCell_Blue")
    mat_pv.diffuse_color = (0.05, 0.1, 0.6, 1.0)
    mat_pv.metallic = 0.2
    mat_pv.roughness = 0.4
    hex_face.data.materials.append(mat_pv)

    # -- Structural frame (6 ribs from center to vertices) --
    for i in range(6):
        angle = math.radians(30 + i * 60)
        x_end = 5.774 * math.cos(angle)
        y_end = 5.774 * math.sin(angle)
        bpy.ops.mesh.primitive_cylinder_add(
            radius=0.03,
            depth=5.774,
            location=(x_end / 2, y_end / 2, 0.0025),
            rotation=(0, math.pi / 2, angle)
        )
        rib = bpy.context.active_object
        rib.name = f"Rib_{i}"
        mat_frame = bpy.data.materials.new(name=f"Mat_Frame_Silver_{i}")
        mat_frame.diffuse_color = (0.7, 0.7, 0.75, 1.0)
        mat_frame.metallic = 0.9
        rib.data.materials.append(mat_frame)

    # -- Attitude thrusters at 6 vertices --
    mat_thruster = bpy.data.materials.new(name="Mat_Thruster_DarkGrey")
    mat_thruster.diffuse_color = (0.15, 0.15, 0.15, 1.0)
    mat_thruster.metallic = 0.6

    for i in range(6):
        angle = math.radians(30 + i * 60)
        x_pos = 5.774 * math.cos(angle)
        y_pos = 5.774 * math.sin(angle)
        bpy.ops.mesh.primitive_cone_add(
            vertices=8, radius1=0.05, radius2=0.02, depth=0.15,
            location=(x_pos, y_pos, 0.1),
            rotation=(0, 0, 0)
        )
        thruster = bpy.context.active_object
        thruster.name = f"Thruster_{i}"
        thruster.data.materials.append(mat_thruster)

    # -- Hub material --
    mat_hub = bpy.data.materials.new(name="Mat_Hub_Titanium")
    mat_hub.diffuse_color = (0.5, 0.5, 0.55, 1.0)
    mat_hub.metallic = 0.95
    hub.data.materials.append(mat_hub)

    print("Dyson Swarm Element geometry created.")
    print(f"Panel hex flat-to-flat: 10m (radius 5.774m)")
    print(f"Panel thickness: 5mm")
    print(f"Attitude thrusters: 6x at hex vertices")
    print(f"Central hub: 0.5m diameter")


def export_stl(filepath="//dyson-swarm-element-v0.stl"):
    bpy.ops.export_mesh.stl(filepath=filepath, use_selection=False)
    print(f"Exported STL: {filepath}")


def export_gltf(filepath="//dyson-swarm-element-v0.gltf"):
    bpy.ops.export_scene.gltf(filepath=filepath, export_format='GLTF_EMBEDDED')
    print(f"Exported glTF: {filepath}")


if __name__ == "__main__":
    create_dyson_swarm_element()
    export_stl()
    export_gltf()

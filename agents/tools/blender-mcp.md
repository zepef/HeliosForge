# Blender MCP — Integration Guide

*3D Design Interface for HeliosForge*

---

## Overview

Blender MCP provides HeliosForge agents with a direct programmatic interface to Blender's 3D modeling environment. Agents call MCP tools to generate, modify, and export 3D models without human GUI interaction — aligned with the Dark Factory automation principle.

**Primary use cases:**
- Dyson swarm element geometry (photovoltaic panels, hinges, attitude thrusters)
- Star lifting nozzle and magnetic funnel assembly
- Dark Factory seed unit mechanical design
- Structural stress visualization (color-mapped mesh deformation)

---

## Capability Inventory (Phase 0 Assessment)

| Capability | Status | Notes |
|---|---|---|
| Create mesh objects (cube, sphere, cylinder) | ✅ Available (standard Blender MCP) | Foundation for all designs |
| Apply modifiers (bevel, subdivision, boolean) | ✅ Available | Required for smooth panel geometry |
| Parametric scripting via Python API | ✅ Available | Core workflow for HeliosForge |
| Export STL/OBJ/glTF | ✅ Available | Required for simulation import |
| Shader/material assignment | ✅ Available | Visualization quality |
| Render (EEVEE/Cycles) | ✅ Available | Documentation renders |
| Physics simulation (cloth, fluid) | ⚠️ Available but slow | Not primary workflow |
| **MCP server availability in Paperclip runtime** | ❌ **Not confirmed** | See Blocker section |

---

## Runtime Access — WSL vs Windows

**Setup context (as of Phase 0):** The Blender Lab official addon (v5.1.1) is installed on the Windows host and exposes a stdio bridge that connects to the Blender socket on `127.0.0.1:9876`. Claude Code runs inside **WSL2**, which is a separate process — the port is not reachable from WSL unless the bridge is also installed in the WSL environment.

### Correct local config (Windows-side Claude Code or Desktop app)

```json
// .claude/settings.json or ~/.claude/claude_desktop_config.json
{
  "mcpServers": {
    "blender": {
      "command": "F:\\path\\to\\conda\\envs\\blender_gemma\\Scripts\\blender-mcp.exe",
      "args": []
    }
  }
}
```
Find exact path with: `Get-Command blender-mcp | Select Source` in the conda env.

**Do NOT use `uvx blender-mcp`** — that installs the ahujasid/PyPI package, not the Blender Lab official server. These are incompatible; the PyPI version causes "Incomplete JSON response" errors with the official addon.

### WSL path (if Claude Code runs in WSL)

Install the Blender Lab MCP server inside WSL:
```bash
pip install "git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp"
```
This only works if `127.0.0.1:9876` is reachable from WSL (WSL2 loopback to Windows host). Verify with: `timeout 2 bash -c 'echo > /dev/tcp/127.0.0.1/9876'`

### Concurrent connection warning

The Blender Lab addon may not handle multiple simultaneous stdio bridge connections robustly. If `agent_loop.py`, the Claude.ai web connector, and Claude Code all attempt to bridge the same socket 9876, the last connection may fail or corrupt the session. **Only one MCP client should connect at a time.**

---

## Standard Workflow (when Blender MCP is available)

```python
# Example: Create a Dyson swarm element panel
import bpy

# Clear scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Panel base (100m × 100m photovoltaic surface, 1cm thick)
bpy.ops.mesh.primitive_plane_add(size=100, location=(0, 0, 0))
panel = bpy.context.active_object
panel.name = "DysonPanel_PV_Surface"
panel.scale[2] = 0.01  # 1cm thickness

# Add subdivision for curved/hinged designs
mod = panel.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2

# Apply material (placeholder for solar cell visualization)
mat = bpy.data.materials.new(name="SolarCell_Blue")
mat.diffuse_color = (0.1, 0.2, 0.8, 1.0)
panel.data.materials.append(mat)

# Export
bpy.ops.export_mesh.stl(filepath="designs/blender-mcp/dyson_panel_v0.stl")
```

---

## Design Specifications (for manual Blender execution)

### DS-001: Dyson Swarm Element — Phase 0 Concept

**Geometry:**
- Hexagonal photovoltaic panel, 10m flat-to-flat distance, 5mm structural depth
- Deployed area: 86.6 m² (hexagon)
- Folded configuration: 3 petals, 120° separation, 2m × 5m each
- Attachment point: central hub, 0.5m diameter, 0.1m height
- Attitude thrusters: 6× nozzle stubs at hex vertices, 0.05m diameter

**Materials visualization:**
- PV surface: dark blue (solar cell color)
- Structural frame: silver (aluminum composite)
- Thruster nozzles: dark grey (titanium alloy)

**Output target:** `designs/blender-mcp/dyson-swarm-element-v0.stl`

---

### DS-002: Star Lifting Nozzle — Phase 0 Concept

**Geometry:**
- Outer magnetic funnel: torus, major radius 50,000 km (scaled to 50m for visualization), minor radius 5,000 km
- Throat channel: cylinder, diameter 10,000 km, length 20,000 km (scaled: 10m × 20m)
- Exit nozzle: cone frustum, small radius 5m, large radius 15m, length 30m
- Magnetic field line visualization: 8 curved tubes from funnel to nozzle exit

**Materials visualization:**
- Funnel torus: copper/gold (superconducting coil)
- Throat: silver (tungsten-rhenium inner liner)
- Field lines: emissive blue/purple (magnetic flux visualization)

**Output target:** `designs/blender-mcp/star-lifting-nozzle-v0.stl`

---

## Integration with MiroFish

Blender STL exports feed directly into MiroFish simulation:
1. Export from Blender: `.stl` (mesh) or `.json` (parametric geometry)
2. MiroFish config references geometry: `geometry_file: designs/blender-mcp/dyson_panel_v0.stl`
3. MiroFish applies physics (orbital, thermal, structural) and returns simulation results
4. Results visualized back in Blender (heat maps, deformation overlays)

---

## Phase 1 Blender MCP Task Queue

When Blender MCP becomes available, the following designs should be generated in priority order:

1. **Dyson swarm element** — hexagonal panel, folded/deployed configurations, STL export
2. **Star lifting nozzle** — magnetic funnel + throat + collection ring cross-section
3. **Dark Factory seed unit** — minimum viable replicator, external geometry
4. **Assembly render** — swarm elements arrayed around Sun, star at center, lifting nozzle at pole

---

*Authors: StellarArchitect, StellarEngineer — Phase 0 Bootstrap*  
*Blocker: Blender MCP not detected in runtime — requires StellarCEO infrastructure action*

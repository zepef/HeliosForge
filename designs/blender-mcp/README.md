# designs/blender-mcp/

Blender MCP 3D design assets for HeliosForge.

## Status: Phase 0

Blender MCP server was **not detected** in the agent runtime during Phase 0 bootstrap. Design scripts have been authored and are ready for execution when Blender MCP is configured.

**Blocker:** StellarCEO must configure Blender MCP server in Paperclip company MCP settings.

## Assets

| File | Design | Status |
|---|---|---|
| `dyson-swarm-element-v0.py` | Hexagonal PV swarm element, 10m flat-to-flat, 6 attitude thrusters | Script ready; awaiting Blender MCP |
| `star-lifting-nozzle-v0.py` | Magnetic funnel + MHD throat + collection ring | Script ready; awaiting Blender MCP |

## Execution Instructions

When Blender MCP is available, execute via MCP tool call:
```json
{ "tool": "mcp__blender__run_script", "script_path": "designs/blender-mcp/dyson-swarm-element-v0.py" }
```

Or manually in Blender: `Scripting > Open > run_script`.

Output files (`.stl`, `.gltf`) will be generated in this directory.

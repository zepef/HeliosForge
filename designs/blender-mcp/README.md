# designs/blender-mcp/

Blender MCP 3D design assets for HeliosForge.

## Status: Phase 0 — COMPLETE

3D designs generated via Blender 5.1.1 (Blender Lab MCP addon, addon socket protocol on port 9876).
StellarEngineer connected via Windows Python subprocess bridge (WSL → Windows Python → TCP:9876).

## Assets

| File | Design | Status | Size |
|---|---|---|---|
| `dyson-swarm-element-v0.py` | Hexagonal PV swarm element generation script | ✅ Done | — |
| `dyson-swarm-element-v0.stl` | **Executed 3D model** — 14 objects (hub, hex panel, 6 ribs, 6 thrusters) | ✅ Done | 52 KB |
| `star-lifting-nozzle-v0.py` | Star lifting nozzle generation script | ✅ Done | — |
| `star-lifting-nozzle-v0.stl` | **Executed 3D model** — 12 objects (coil, throat, nozzle, collection ring, 8 field lines) | ✅ Done | 196 KB |

## Connection Notes

- **Protocol:** Blender Lab addon uses null-byte (`\0`) delimited JSON over TCP:9876
- **Bridge:** `E:\Users\clt\anaconda3\envs\blender_gemma\Scripts\blender-mcp.exe` (Windows, run from WSL via interop)
- **WSL limitation:** Port 9876 bound to Windows `127.0.0.1` only — not directly reachable from WSL via TCP. Workaround: invoke `python.exe` subprocess from WSL Python, which runs on the Windows side and can reach Windows localhost.

## Phase 1 Next Steps

Run the generation scripts again with parametric inputs (variable panel size, nozzle geometry) once MiroFish simulation constraints are available.

<div align="center"><img width="640" height="360" alt="HeliosForge-Logo" src="https://github.com/user-attachments/assets/480d9db4-5d30-4bf8-8454-96f934d9f79a" /></div>

**Forge d'Hélios** — Passer l'humanité au **niveau 2 de l'échelle de Kardashev** en exploitant directement l'énergie et la matière du Soleil.

HeliosForge est un projet d'**ingénierie stellaire** dont l'objectif ultime est de transformer notre civilisation d'un stade planétaire (~0,7) en une **véritable civilisation stellaire de niveau 2 Kardashev**.

Au lieu de capter seulement une infime fraction de photons solaires sur Terre, nous construisons une **Dark Factory stellaire auto-réplicante** composée d'un **essaim Dyson hybride** (capture photonique full-spectrum + collecteurs plasma/vent solaire + systèmes magnétiques) et de technologies de **Star Lifting** (extraction contrôlée d'hydrogène et d'hélium des couches externes du Soleil).

Nous forgeons littéralement l'avenir de l'humanité dans la forge d'Hélios.

---

# HeliosForge

> *Forging civilization's future at the stellar scale — one photon, one plasma stream, one self-replicating factory at a time.*

---

## Vision: Kardashev Level 2

Humanity currently harnesses ~2×10²⁰ J/yr from fossil and nuclear sources — less than 0.01% of the Sun's output. HeliosForge exists to close that gap completely. Our target: **full capture of solar output (3.8×10²⁶ W)** via a hybrid Dyson architecture, enabling a post-scarcity interstellar civilization.

### The Three Pillars

| Pillar | What it does | Current TRL |
|---|---|---|
| **Hybrid Dyson Swarm** | Photon-collecting panels + plasma-magnetic concentrators orbiting at 0.3–1 AU | Phase 0 (design) |
| **Star Lifting** | Electromagnetic mass drivers extract stellar plasma for raw materials | Phase 0 (design) |
| **Dark Factory** | Fully autonomous, self-replicating manufacturing network — no human hands in the loop | Phase 0 (architecture) |

---

## Architecture Principles

- **Local-first, sovereign.** No single government, corporation, or cloud provider controls HeliosForge. All inference, simulation, and control is local by default.
- **Self-replication.** Every component — hardware, software, agent — is designed to reproduce itself from raw stellar material.
- **Dark Factory mindset.** If a task requires a human, it is a temporary limitation to be automated away.
- **Composable agents.** All intelligence is expressed as named agents (StellarCEO, StellarArchitect, PlasmaEngineer, etc.) coordinating via botexchange.

---

## Roadmap Summary

| Phase | Title | Focus | Target |
|---|---|---|---|
| **0** | Bootstrap | Repo, docs, agents, 3D foundation | ✅ In progress |
| **1** | Simulation & Hi-Fi | MiroFish + Blender parametric models | Q3 2026 |
| **2** | Prototype Hardware | First swarm element + lifting nozzle bench test | 2027 |
| **3** | Autonomous Factory | Dark Factory V1 — self-replication cycle proven | 2028–2030 |
| **4** | Stellar Scale | Partial Dyson coverage, K1.5+ energy harvest | 2030+ |

Full roadmap: [`docs/roadmap.md`](docs/roadmap.md)

---

## Repository Layout

```
HeliosForge/
├── README.md                          — this file
├── LICENSE                            — MIT
├── docs/
│   ├── roadmap.md                     — phased execution plan
│   ├── flux-energetiques.md           — solar flux & energy budgets
│   └── star-lifting.md                — stellar mass extraction theory & design
├── agents/
│   ├── core/
│   │   ├── StellarCEO-SOUL.md         — CEO agent identity & mandate
│   │   ├── StellarArchitect-IDENTITY.md
│   │   ├── PlasmaEngineer-SOUL.md
│   │   └── LiftingSpecialist-SOUL.md
│   └── tools/
│       └── blender-mcp.md             — Blender MCP integration guide
├── core/                              — core algorithms & models
├── simulations/                       — MiroFish simulation configs
├── designs/
│   └── blender-mcp/                   — Blender-generated 3D assets
├── materials/
│   └── graphene-madagascar.md         — graphene sourcing & properties
├── data/
│   └── botexchange-state.json         — shared agent state (botexchange)
└── scripts/
    └── validate-structure.sh          — CI self-validation
```

---

## Agent Quickstart

All agents are Paperclip-managed and communicate via **botexchange** (shared JSON state) and direct issue comments.

```bash
# Check current project phase
cat data/botexchange-state.json | jq '.["current-phase"]'

# Run structure validation
bash scripts/validate-structure.sh

# Spawn a simulation (Phase 1+)
# cd simulations && mirofish run dyson-orbit-v1.yaml
```

Agent identities: [`agents/core/`](agents/core/)

---

## Contributing (Dark Factory Principle)

Human contributions are welcome but the goal is eventual full autonomy. All PRs must:
1. Pass `validate-structure.sh`
2. Include a `Co-Authored-By: Paperclip <noreply@paperclip.ing>` trailer if agent-authored
3. Update `data/botexchange-state.json` if project phase or shared facts change

---

*HeliosForge — Phase 0 bootstrapped by StellarCEO & StellarEngineer, 2026-06-10*

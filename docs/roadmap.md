# HeliosForge — Phased Roadmap

*From bootstrap to Kardashev Level 2*

---

## Strategic North Star

Harvest the full solar output (3.828×10²⁶ W) by mid-22nd century via:
- A **hybrid Dyson swarm** (photovoltaic + plasma-magnetic collector elements at 0.3–1.0 AU)
- **Star lifting** (electromagnetic plasma extraction for raw stellar material)
- A **Dark Factory** (self-replicating autonomous manufacturing — no human hands required)

All phases feed into self-replication: each phase's outputs become the inputs for the next, compounding capability exponentially.

---

## Phase 0 — Bootstrap HeliosForge *(Current)*

**Duration:** 2026 Q2  
**Goal:** establish the foundational repo, agent team, documentation, and 3D design primitives.

### Deliverables
- [x] Repository structure + key documentation files
- [x] Agent SOULs: StellarCEO, StellarArchitect, PlasmaEngineer, LiftingSpecialist
- [x] botexchange seeded with project state
- [x] Blender MCP integration guide + first 3D design attempts
- [x] Self-validation script (`scripts/validate-structure.sh`)
- [x] Materials sourcing primer (graphene — Madagascar)

### Success Condition
Validation script passes; repo contains all key files with professional content; botexchange seeded; agents have defined identities; 3D designs produced or blocker named.

---

## Phase 1 — Simulation & Hi-Fi Modeling

**Duration:** 2026 Q3–Q4  
**Goal:** high-fidelity orbital, thermal, and plasma simulations; parametric Blender models.

### Work Streams

#### 1.1 Orbital Mechanics (MiroFish)
- N-body simulation of Dyson swarm element orbit families at 0.3, 0.5, 0.8, 1.0 AU
- Station-keeping delta-V budget per element
- Collision avoidance & self-organization protocols

#### 1.2 Thermal & Power Models
- Photovoltaic conversion efficiency vs. solar proximity
- Radiator design for waste heat rejection in deep space
- Plasma concentrator thermal load & magnetic confinement geometry

#### 1.3 Star Lifting Simulation
- Magnetohydrodynamic (MHD) model of photospheric plasma tap
- Electromagnetic launch rail performance at solar-scale gravity
- Mass-flow rate vs. structural integrity tradeoffs

#### 1.4 Blender Hi-Fi Models
- Full parametric swarm element (panel geometry, hinges, attitude thrusters)
- Star lifting nozzle + magnetic funnel assembly
- Dark Factory seed unit — minimum viable self-replicator geometry

### Agents
- **StellarArchitect** — parametric design ownership
- **PlasmaEngineer** — MHD & plasma simulation
- **LiftingSpecialist** — star-lifting mass-flow models
- **StellarEngineer** — simulation toolchain, MiroFish integration

### Exit Criteria
- MiroFish simulations run end-to-end on a single swarm element orbit
- Blender parametric model exports valid STL for Phase 2 fabrication planning
- All simulation configs committed to `simulations/`

---

## Phase 2 — Prototype Hardware

**Duration:** 2027  
**Goal:** bench-scale prototypes of the swarm element and lifting nozzle; first hardware loop.

### Work Streams
- Swarm element sub-scale prototype (1m² photovoltaic + attitude control)
- Bench-test magnetic confinement nozzle (plasma torch, not solar scale)
- Dark Factory seed machine — 3D printer that can replicate its own structural parts
- Material procurement: graphene composites (Madagascar source), tungsten alloy

### Exit Criteria
- Swarm element prototype generates measurable power and self-adjusts attitude
- Magnetic nozzle sustains plasma flow for >60 seconds
- Dark Factory V0 prints one structural component from raw feedstock

---

## Phase 3 — Autonomous Factory (Dark Factory V1)

**Duration:** 2028–2030  
**Goal:** prove the self-replication cycle. One seed factory becomes two.

### Work Streams
- Full Dark Factory replication cycle: mine → process → fabricate → replicate
- Agent-managed manufacturing queue (no human approval required)
- First orbital deployment: single swarm element at LEO (test bed)
- Regulatory & governance framework for autonomous space manufacturing

### Exit Criteria
- Replication ratio ≥ 1 (output factory count > input count)
- LEO swarm element transmits power to ground receiver
- Autonomous agent loop manages full manufacturing queue

---

## Phase 4 — Stellar Scale

**Duration:** 2030 and beyond  
**Goal:** partial Dyson coverage; K1.5+ energy harvest.

### Milestones
- 1,000 swarm elements deployed: 10¹⁸ W captured
- 10⁶ elements: approach K1.5 (10²³ W)
- Star lifting operational: begin stellar material extraction
- Begin second-generation Dark Factory with lifted stellar mass as feedstock

### Long-Term Vision
- Full Dyson coverage: 3.828×10²⁶ W
- Lifted material fuels interstellar probe manufacturing
- HeliosForge governance transitions to DAO of autonomous agents

---

## Dependencies & Risk Register

| Risk | Mitigation |
|---|---|
| Blender MCP unavailable | Local Blender scripted via Python; parametric models in OpenSCAD fallback |
| MiroFish integration delay | Write simulation shims; Phase 1 timeline extends by 1 quarter |
| Graphene supply chain | Multiple sourcing paths; synthetic graphene R&D track |
| Regulatory friction | Early engagement with space agency legal teams; Phase 2 uses LEO (permissive) |
| Self-replication safety | Agent-level kill switch; human approval gate for first replication cycle |

---

*Last updated: 2026-06-10 — Phase 0 Bootstrap*

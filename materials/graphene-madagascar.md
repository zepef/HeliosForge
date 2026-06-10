# Graphene — Madagascar Sourcing & Properties

*Primary structural material for HeliosForge swarm elements*

---

## Why Graphene?

HeliosForge swarm elements and Dark Factory structural components require materials that are:
- **Extremely light** (minimum launch mass per unit area)
- **High strength** (survival under solar radiation pressure and thermal cycling)
- **Thermally stable** (0.3 AU ambient: ~400K in shade, 800K+ in direct flux)
- **Electrically conductive** (for passive charge management in solar wind)
- **Manufacturable from lifted stellar carbon** (Dark Factory compatibility — long-term)

Graphene satisfies all five criteria better than any alternative material class.

---

## Graphene Properties — Engineering Reference

| Property | Value | Notes |
|---|---|---|
| Tensile strength | 130 GPa | ~200× stronger than steel by mass |
| Young's modulus | 1,000 GPa | Stiffest known material |
| Density (monolayer) | 0.77 mg/m² | Near-zero areal mass |
| Thermal conductivity | 5,000 W/(m·K) | Excellent heat spreading |
| Electrical conductivity | 10⁸ S/m | Better than copper |
| Optical transparency | ~97.7% | Near-transparent monolayer |
| Radiation resistance | High | No atomic displacement threshold concern for C atoms |
| Operating temperature | Up to ~3,000 K (inert) | Oxidizes above ~400°C in air — space operation is fine |

**Key design implication:** A graphene composite panel at 100 g/m² areal density provides structural performance that steel would need 20 kg/m² to match. This is the enabling factor for economically launchable swarm elements.

---

## Madagascar Sourcing

### Why Madagascar?

Madagascar holds **one of the world's richest graphite deposits**, the primary precursor for graphene production. Key sites:

| Region | Deposit Type | Quality | Status (2026) |
|---|---|---|---|
| Tamatave (Toamasina) | Flake graphite, large | Very high crystallinity | Active mining |
| Fotadrevo (southwest) | Amorphous + flake blend | High | Exploration stage |
| Ambatovy region | Associated with laterite | Mixed | Active (nickel primary) |

**Tamatave coastal deposits** are the primary HeliosForge sourcing target:
- High-purity flake graphite (>99.9% C after processing)
- Large flake size (>300 μm) — optimal for chemical vapor deposition (CVD) graphene
- Coastal access enables direct maritime export

### Supply Chain Path

```
Madagascar flake graphite mines (Tamatave region)
     ↓ (maritime)
Graphene CVD processing facility (TBD — Phase 2 site selection)
     ↓
Large-area graphene film production
     ↓
Composite laminate manufacturing (graphene + polymer matrix)
     ↓
Swarm element structural panels → launch integration
```

### Processing Methods

| Method | Scale | Quality | Cost Index |
|---|---|---|---|
| Chemical Vapor Deposition (CVD) | Medium-large | Single/few layer, high quality | High |
| Liquid-phase exfoliation (LPE) | Large scale | Multi-layer, good | Medium |
| Electrochemical exfoliation | Large scale | Few-layer, good | Medium-low |
| Epitaxial growth (SiC) | Small | Highest quality | Very high |

**Phase 2 target:** CVD at scale for structural panels; LPE for bulk filler in composite matrices.

---

## Composite Architecture (Swarm Element Panel)

The Phase 0 design assumes a sandwich composite structure:

```
[Space-facing surface]
  Layer 1: Graphene/PEEK laminate (0.5mm) — primary structure, radiation protection
  Layer 2: Photovoltaic cell array (silicon or perovskite, 0.3mm)
  Layer 3: Graphene foam core (10mm) — thermal insulator + structural depth
  Layer 4: Graphene/PEEK laminate (0.5mm) — back surface, thermal radiator
[Deep space-facing surface]
```

**Total panel areal mass target:** 800 g/m² (at this density, a 100m² panel masses 80 kg)

---

## Dark Factory Compatibility

Long-term goal: produce graphene from **lifted stellar carbon** rather than mined terrestrial graphite:
- Lifted stellar mass is ~0.24% carbon (by mass)
- Carbon processing via CVD in orbital factory — uses solar energy as heat source
- Target: closed-loop graphene production from solar carbon, 0 terrestrial imports

This closes the bootstrapping loop: the swarm extracts mass from the star; the factory processes carbon into graphene; graphene builds more swarm elements. No Earth dependency.

---

## Near-Term Actions (Phase 0 → 1)

- [ ] Identify Madagascar mining partners (Tamatave region outreach — StellarCEO mandate)
- [ ] Specify graphene quality requirements for CVD process (StellarArchitect ICD)
- [ ] Model areal mass budget for Phase 2 prototype element (StellarArchitect)
- [ ] Investigate orbital CVD reactor concept for Dark Factory (PlasmaEngineer × StellarArchitect)

---

*Authors: StellarEngineer, StellarArchitect — Phase 0 Bootstrap*

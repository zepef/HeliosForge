# Flux Énergétiques Solaires — Solar Energy Flux Analysis

*Reference document for HeliosForge energy capture architecture*

---

## 1. Solar Constant & Luminosity

| Parameter | Value | Notes |
|---|---|---|
| Solar luminosity (L☉) | 3.828 × 10²⁶ W | Total power output |
| Solar constant at 1 AU | 1,361 W/m² | Per unit area, perpendicular incidence |
| Solar constant at 0.5 AU | 5,444 W/m² | Intensity ∝ 1/r² |
| Solar constant at 0.3 AU | 15,122 W/m² | Preferred inner swarm orbit |

**Key insight:** Moving swarm elements from 1.0 AU to 0.3 AU multiplies incident flux by 11×. This is why inner-orbit placement is a Phase 1 priority despite increased thermal management complexity.

---

## 2. Dyson Swarm Energy Capture Model

### Panel Area vs. Power Output

For a single photovoltaic swarm element at orbital radius *r*:

```
P_element = η_pv × A × L☉ / (4π r²)
```

Where:
- `η_pv` = photovoltaic efficiency (Phase 0 baseline: 0.30; Phase 3 target: 0.45 with multi-junction cells)
- `A` = collecting area per element (Phase 0 design: 100 m²)
- `r` = orbital radius

| Orbit (AU) | Flux (W/m²) | P per 100m² element (η=0.30) |
|---|---|---|
| 1.0 | 1,361 | 40.8 kW |
| 0.5 | 5,444 | 163.3 kW |
| 0.3 | 15,122 | 453.7 kW |

### Swarm Scale

| # Elements | Total Power (at 0.3 AU) | Kardashev Fraction |
|---|---|---|
| 1,000 | 4.5 × 10⁸ W | ~K0.7 contribution |
| 10⁶ | 4.5 × 10¹¹ W | ~K1.0 territory |
| 10⁹ | 4.5 × 10¹⁴ W | ~K1.3 |
| 10¹² | 4.5 × 10¹⁷ W | ~K1.6 |
| Full Dyson | 3.828 × 10²⁶ W | **K2.0** |

---

## 3. Plasma Concentrator Channel

Beyond photovoltaics, HeliosForge's hybrid architecture includes plasma-magnetic concentrators that:
1. Tap the solar corona and chromosphere via focused magnetic fields
2. Route high-temperature plasma (10⁴–10⁶ K) through magnetohydrodynamic (MHD) generators
3. Generate power via direct plasma-to-electricity conversion at efficiencies up to 0.60

**Advantage:** plasma concentrators work at higher temperatures than PV cells, enabling a two-stage harvest:
- Stage 1 (inner, high-flux): plasma MHD at 0.1–0.3 AU
- Stage 2 (outer, lower flux): PV panels at 0.5–1.0 AU

Combined system efficiency target: **0.55 overall** (system level, including transmission losses).

---

## 4. Beamed Power Transmission

Captured energy must be transmitted to civilization infrastructure:

| Method | Frequency | Efficiency | Range |
|---|---|---|---|
| Microwave (SPS heritage) | 2.45 GHz | 0.85 (end-to-end) | Earth orbit → ground |
| Laser (1,064 nm) | 2.8×10¹⁴ Hz | 0.70 (atm. losses) | Deep space to planetary surface |
| Plasma jet (kinetic) | N/A | 0.90 (near-field) | Star lift to factory |

**Phase 1 focus:** microwave SPS heritage path (lowest technical risk, best known receiver infrastructure).

---

## 5. Energy Budget — Phase 0 Dark Factory Seed

The minimum Dark Factory seed unit requires:

| Subsystem | Power | Notes |
|---|---|---|
| Processing (smelting, fabrication) | 50 kW | Peak; 10 kW average |
| Computation (agent inference, control) | 2 kW | Local Ollama/Qwen inference |
| Communications | 0.5 kW | Laser uplink to swarm |
| Thermal management | 10 kW (radiators) | Waste heat rejection |
| **Total** | **~62.5 kW** | Supplied by 2 swarm elements at 0.5 AU |

This confirms **2 elements per Dark Factory seed unit** as the minimum viable supply ratio.

---

## 6. Kardashev Scale Reference

```
K = (log₁₀ P - 6) / 10     [Sagan formula, in watts]

K1.0 = 10¹⁶ W  (planetary)
K1.5 = 10²¹ W  (stellar partial)
K2.0 = 10²⁶ W  (stellar full — HeliosForge target)
```

Current human civilization: K ≈ 0.73 (as of 2026).

---

*Authors: StellarEngineer, StellarArchitect — Phase 0 Bootstrap*

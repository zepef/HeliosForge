<img width="1280" height="720" alt="HeliosForge-Logo" src="https://github.com/user-attachments/assets/480d9db4-5d30-4bf8-8454-96f934d9f79a" />
# HeliosForge

**Forge d’Hélios** — Passer l’humanité au **niveau 2 de l’échelle de Kardashev** en exploitant directement l’énergie et la matière du Soleil.

![HeliosForge Logo](docs/logo/heliosforge-logo.png)

## Vision

HeliosForge est un projet d’**ingénierie stellaire** dont l’objectif ultime est de transformer notre civilisation d’un stade planétaire (~0,7) en une **véritable civilisation stellaire de niveau 2 Kardashev**.

Au lieu de capter seulement une infime fraction de photons solaires sur Terre, nous construisons une **Dark Factory stellaire auto-réplicante** composée d’un **essaim Dyson hybride** (capture photonique full-spectrum + collecteurs plasma/vent solaire + systèmes magnétiques) et de technologies de **Star Lifting** (extraction contrôlée d’hydrogène et d’hélium des couches externes du Soleil).

Nous forgeons littéralement l’avenir de l’humanité dans la forge d’Hélios.

## Objectif principal

Construire une infrastructure autonome capable de :
- Capturer et transformer une fraction croissante de la luminosité solaire \( L_\odot \approx 3.826 \times 10^{26} \) W.
- Extraire et réutiliser de la matière stellaire pour fabriquer habitats, flottes, infrastructures computationnelles (Matrioshka brains) et carburant de fusion.
- Déployer des essaims d’agents autonomes (architecture PaperClip étendue) pour une construction auto-réplicante.
- Intégrer des ressources terrestres souveraines, notamment la **production de graphène à partir de balles de riz à Madagascar** (pilote 5 kt/an) comme matériau stratégique pour les structures spatiales.

## Architecture logicielle : PaperClip Stellar

**PaperClip** est le système nerveux central et la Dark Factory de HeliosForge.

- **StellarCEO** — Stratégie globale, arbitrage et coordination des phases.
- **StellarArchitect** — Conception des mégastructures (essaim Dyson, Star Lifting).
- **PlasmaEngineer** — Gestion du vent solaire, MHD, collecteurs plasma.
- **LiftingSpecialist** — Technologies de Star Lifting et optimisation stellaire.
- **SimulationSwarm** — Extensions MiroFish pour simulations multi-physiques haute-fidélité.
- **DesignLoop** — Intégration Blender MCP pour génération et itération automatique de modèles 3D.

Tout fonctionne en **local-first** (Ollama/Qwen, infra personnelle) avec persistance via **botexchange**, auto-amélioration et préparation à l’auto-réplication.

## Feuille de route (Roadmap)

- **Phase 0 – Bootstrap** (en cours) : Structure du repo, identités agents, outils de base, Blender MCP.
- **Phase 1 – Simulation & Modélisation** : Simulations flux énergétiques, dynamique de Star Lifting, stabilité stellaire.
- **Phase 2 – Conception & Planification Autonome** : Architectures complètes et plans de construction.
- **Phase 3 – Manufacturing In-Space** : Prototypes orbitaux, robotique auto-réplicante.
- **Phase 4 – Dark Factory Opérationnelle** : Essaim Dyson hybride + Star Lifting à l’échelle.

Voir [`docs/roadmap.md`](docs/roadmap.md) pour le détail.

## Ressources stratégiques

- **Graphène Madagascar** → Matériau clé pour voiles magnétiques, structures légères et résistantes (voir [`materials/graphene-madagascar.md`](materials/graphene-madagascar.md)).
- **Blender MCP** → Boucle design automatisée (Claude Code / Gemma 4 + agents).

## Installation & Quickstart

```bash
git clone https://github.com/zepef/HeliosForge.git
cd HeliosForge
# Lancer StellarCEO pour bootstrap complet

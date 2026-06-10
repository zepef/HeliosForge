#!/usr/bin/env bash
# HeliosForge Phase 0 — Structure Validation Script
# Verifies repo layout and key files are present and non-empty.
# Exit 0: pass. Exit 1: fail (lists missing/empty items).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PASS=0
FAIL=0
FAILURES=()

check_exists() {
  local path="$REPO_ROOT/$1"
  if [ -e "$path" ]; then
    echo "  [OK] $1"
    ((PASS++)) || true
  else
    echo "  [FAIL] MISSING: $1"
    FAILURES+=("MISSING: $1")
    ((FAIL++)) || true
  fi
}

check_nonempty() {
  local path="$REPO_ROOT/$1"
  if [ -f "$path" ] && [ -s "$path" ]; then
    echo "  [OK] $1 (non-empty)"
    ((PASS++)) || true
  elif [ ! -f "$path" ]; then
    echo "  [FAIL] MISSING: $1"
    FAILURES+=("MISSING: $1")
    ((FAIL++)) || true
  else
    echo "  [FAIL] EMPTY: $1"
    FAILURES+=("EMPTY: $1")
    ((FAIL++)) || true
  fi
}

check_dir() {
  local path="$REPO_ROOT/$1"
  if [ -d "$path" ]; then
    echo "  [OK] $1/"
    ((PASS++)) || true
  else
    echo "  [FAIL] MISSING DIR: $1"
    FAILURES+=("MISSING DIR: $1")
    ((FAIL++)) || true
  fi
}

echo "========================================"
echo " HeliosForge Phase 0 — Structure Check"
echo " Repo: $REPO_ROOT"
echo "========================================"
echo ""

echo "--- Directories ---"
check_dir "docs"
check_dir "agents/core"
check_dir "agents/tools"
check_dir "core"
check_dir "simulations"
check_dir "designs/blender-mcp"
check_dir "materials"
check_dir "data"
check_dir "scripts"

echo ""
echo "--- Root Files ---"
check_nonempty "README.md"
check_nonempty "LICENSE"

echo ""
echo "--- Documentation ---"
check_nonempty "docs/roadmap.md"
check_nonempty "docs/flux-energetiques.md"
check_nonempty "docs/star-lifting.md"

echo ""
echo "--- Agent SOULs & Identities ---"
check_nonempty "agents/core/StellarCEO-SOUL.md"
check_nonempty "agents/core/StellarArchitect-IDENTITY.md"
check_nonempty "agents/core/PlasmaEngineer-SOUL.md"
check_nonempty "agents/core/LiftingSpecialist-SOUL.md"

echo ""
echo "--- Agent Tools ---"
check_nonempty "agents/tools/blender-mcp.md"

echo ""
echo "--- Materials ---"
check_nonempty "materials/graphene-madagascar.md"

echo ""
echo "--- Data / botexchange ---"
check_nonempty "data/botexchange-state.json"

# Validate botexchange JSON is parseable
if command -v python3 &>/dev/null; then
  if python3 -c "import json,sys; json.load(open('$REPO_ROOT/data/botexchange-state.json'))" 2>/dev/null; then
    echo "  [OK] data/botexchange-state.json is valid JSON"
    ((PASS++)) || true
  else
    echo "  [FAIL] data/botexchange-state.json is invalid JSON"
    FAILURES+=("INVALID JSON: data/botexchange-state.json")
    ((FAIL++)) || true
  fi
else
  echo "  [SKIP] python3 not available — skipping JSON validation"
fi

echo ""
echo "--- 3D Designs ---"
check_nonempty "designs/blender-mcp/dyson-swarm-element-v0.py"
check_nonempty "designs/blender-mcp/star-lifting-nozzle-v0.py"
check_nonempty "designs/blender-mcp/README.md"

echo ""
echo "--- Scripts ---"
check_nonempty "scripts/validate-structure.sh"

echo ""
echo "========================================"
echo " Results: ${PASS} passed, ${FAIL} failed"
echo "========================================"

if [ "${FAIL}" -gt 0 ]; then
  echo ""
  echo "FAILURES:"
  for f in "${FAILURES[@]}"; do
    echo "  - $f"
  done
  exit 1
else
  echo ""
  echo "ALL CHECKS PASSED — HeliosForge Phase 0 structure is valid."
  exit 0
fi

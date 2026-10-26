# uv - Archived Notes (99 Archive)

This directory contains legacy, historical, or pre-migration notes and artifacts related to the uv Python package and project manager.

---

## 🏛️ Archive Status & Migration Notice

In accordance with the KMS Three-Layer Model and the Archive Retention Policy, all active, unorganized legacy notes and draft notebooks previously held in quarantine under `software/uv/99-archive/` have been audited, synthesized, and migrated to their canonical locations across the KMS.

---

## 🗺️ Canonical Routing Matrix

To locate active, maintained knowledge previously stored in legacy archive folders, refer to the following canonical destinations:

### 1. Layer 1: Software-Centric Knowledge (`software/uv/`)
- **Core uv Manuals, CLI Commands & Operational Workflows**:
  - Canonical Guides: [`00-overview.md`](../00-overview.md), [`01-installation.md`](../01-installation.md), [`02-core-concepts.md`](../02-core-concepts.md), [`03-workflows.md`](../03-workflows.md), [`04-commands.md`](../04-commands.md), [`06-troubleshooting.md`](../06-troubleshooting.md).

### 2. Layer 2: Cross-Cutting Knowledge (`concepts/`, `patterns/`, `meta_learning/`)
- **Modern Python Tooling & Package Management Architecture**:
  - Canonical Location: [`meta_learning/01-software-build-out-checklist.md`](../../meta_learning/01-software-build-out-checklist.md).
- **Package Management & Virtual Environment Concepts**:
  - Canonical Location: [`concepts/package_management/README.md`](../../concepts/package_management/README.md).

### 3. Layer 3: Active Learning Workspace (`active_learning/`)
- **Active Learning Automation Pipelines**:
  - Canonical Location: [`active_learning/research/README.md`](../../active_learning/research/README.md).

---

## 📜 Archive Retention Policy & Guidelines

1. **Superseded Records Only:** Retain only superseded historical drafts or diff baselines that have been fully extracted and synthesized into canonical modules.
2. **Zero Duplicate Maintenance:** Never maintain duplicate active knowledge inside `99-archive/`.
3. **Automated Discovery Hygiene:** Pruning obsolete unindexed quarantine folders ensures automated agents and human search queries return single authoritative sources of truth.
4. **Data-Centric Rule:** Like all KMS directories, archives must never contain `.venv` virtual environments or IDE metadata.

---

**Tags:** #software #uv #archive #history #migration #three_layer_model

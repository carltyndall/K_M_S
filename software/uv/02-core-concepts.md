# uv Core Concepts

## Architectural Mental Model

uv is an extremely fast Python package and project manager written in Rust, designed to replace `pip`, `pip-tools`, and `virtualenv` workflows with deterministic, high-throughput dependency resolution.

---

## 🏛️ Pure Theory & Decoupled Concepts

> **DRY Architecture Rule:** Broad environment management and isolation theories are centralized in Layer 2 (`concepts/`).

- **Environment Isolation:** [`concepts/environment/01-environment-fundamentals.md`](../../concepts/environment/01-environment-fundamentals.md) — Virtual environment state, path resolution, and interpreter decoupling.
- **Dependency & Configuration Management:** [`concepts/configuration_management/`](../../concepts/configuration_management/README.md) — Declarative dependency specifications and lockfile determinism.

---

## ⚙️ uv Tool-Specific Concepts & Mechanics

### 1. High-Performance Resolution Engine (PubGrub)
uv features a Rust-based dependency resolver implementing the PubGrub algorithm. It explores version constraints, performs Boolean SAT backtracking, and resolves valid version sets orders of magnitude faster than legacy resolvers.

### 2. Universal Lockfile Architecture (`uv.lock`)
A cross-platform, deterministic lockfile storing exact wheel hashes, source distribution metadata, and transitive resolution trees. It guarantees 100% reproducible environments across macOS, Linux, and Windows.

### 3. Global Cache & Hardlink Linking
uv maintains a global wheel and source cache in `~/.cache/uv`. When instantiating new virtual environments on supported filesystems (APFS, NTFS, ext4), uv uses hardlinks or clonefile (reflink) operations to create environments in milliseconds with zero extra disk space.

---

## 🔗 Related Resources

- **Layer 1 Software Guides:**
  - [`software/uv/00-overview.md`](./00-overview.md) — Overview and positioning.
  - [`software/uv/01-installation.md`](./01-installation.md) — Installation and shell setup.
  - [`software/uv/03-workflows.md`](./03-workflows.md) — Project initialization and lock workflows.
  - [`software/uv/04-commands.md`](./04-commands.md) — Command reference and cheat sheet.
  - [`software/uv/06-troubleshooting.md`](./06-troubleshooting.md) — Cache and lock resolution fixes.
- **Layer 2 Concepts & Workflows:**
  - [`concepts/environment/01-environment-fundamentals.md`](../../concepts/environment/01-environment-fundamentals.md) — Virtual environment foundations.
  - [`cheat_sheets/`](../../cheat_sheets/README.md) — High-density syntax lookup.

---
**Tags:** #software #uv #python #resolver #pubgrub #virtualenv #lockfile #architecture

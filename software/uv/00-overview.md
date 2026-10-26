# uv Overview

## Purpose
uv is an extremely fast Python package and project manager, written in Rust. In the context of KMS, it serves as the underlying engine for environment management and is central to the `km-uv` automation tool.

## Mental Models
- **Unified Tooling:** A single tool that replaces `pip`, `pip-tools`, and `virtualenv`.
- **Performance First:** Designed for speed, often 10-100x faster than traditional tools.
- **Reproducibility:** Uses a lockfile (`uv.lock`) to ensure consistent environments across machines.

## Tool Integration
- **km-uv:** The automation layer for KMS that leverages `uv` for all Python-related tasks.
- **PyCharm:** Used to manage the virtual environments that PyCharm uses for development.
- **KMS Root:** Used to manage global and project-specific dependencies without cluttering the data repository with `.venv` folders.

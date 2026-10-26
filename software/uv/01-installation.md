# uv Installation & Configuration

## Environment Setup

### 1. Windows Installation (PowerShell / WinGet)
```powershell
# Standalone installer via PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via Windows Package Manager
winget install --id Astral-sh.uv
```

### 2. macOS Installation (Homebrew / Curl)
```bash
# Via Homebrew
brew install uv

# Or via standalone POSIX installer
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Linux Installation (Curl)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Configuration & Runtime Decoupling

### 1. Global & Project Configuration
- **Global Config:** Located in `%APPDATA%\uv` (Windows) or `~/.config/uv/` (macOS/Linux).
- **Project Governance:** Configured via `pyproject.toml` and locked deterministically via `uv.lock`.

### 2. External Runtime Governance & Zero-`.venv` Repository Purity
- **Architecture Portability Hazard:** Python virtual environments contain architecture-compiled binary wheels (`x86_64-pc-windows-msvc` on Windows vs. `aarch64-apple-darwin` on macOS). Committing `.venv` to version control creates immediate crashes (`Bad CPU type in executable`).
- **KMS Standard:** Virtual environments must NEVER reside within the KMS repository. Store all execution runtimes externally:
  - Windows: `C:\Users\<user>\dev\venvs\`
  - macOS / Linux: `~/dev/venvs/`
- **Automation Integration (`km-uv`):** The `km-uv` automation engine orchestrates external environments and invokes `uv run` or `uv sync` pointing to external directories.

---

## Core CLI Workflows

```bash
# Initialize a new project with pyproject.toml
uv init my_project

# Add dependencies and automatically resolve uv.lock
uv add pandas numpy

# Sync dependencies into external runtime without modifying KMS tree
uv sync

# Run tool without polluting local directories
uv run --no-project python script.py
```

---

## 🔗 Related Resources

- **Layer 1 Software Guides:**
  - [`software/homebrew/00-overview.md`](../homebrew/00-overview.md) — Homebrew package management on macOS.
  - [`software/windows_11/04-commands.md`](../windows_11/04-commands.md) — Windows package management and environment syntax.
- **Layer 2 Workflows & Cheat Sheets:**
  - [`workflows/08-external-python-environments.md`](../../workflows/08-external-python-environments.md) — External Python runtime architecture.
  - [`cheat_sheets/cross-platform-workstation-cheat-sheet.md`](../../cheat_sheets/cross-platform-workstation-cheat-sheet.md) — Multi-OS command matrix.
- **Layer 3 Active Learning & Research:**
  - [`active_learning/research/impact-of-macos-on-knowledge-management.md`](../../active_learning/research/impact-of-macos-on-knowledge-management.md) — Research on execution runtime decoupling.

---

**Tags:** #software #uv #python #package-manager #virtualenv #cross-platform #arm64 #x86_64

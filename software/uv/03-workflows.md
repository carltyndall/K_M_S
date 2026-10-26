# uv Workflows

## Initializing a Project
1. Run `uv init` to create a new `pyproject.toml`.
2. Add dependencies using `uv add <package>`.
3. uv automatically creates a virtual environment and a lockfile.

## Updating Dependencies
1. Modify `pyproject.toml` if needed.
2. Run `uv sync` to align the virtual environment with the lockfile and `pyproject.toml`.
3. Run `uv lock --upgrade` to update all dependencies to their latest compatible versions.

---

## 📦 Building and Publishing Packages (`uv build` & `uv publish`)

`uv` provides extremely fast, standalone package building and distribution capabilities compliant with standard PEP 517/518 build specifications.

### 1. Build Compilation Workflow
Build both Source Distribution (`sdist`) and Wheel (`wheel`) into `dist/`:

```bash
# Compile both sdist and wheel
uv build

# Compile specific artifact types
uv build --sdist
uv build --wheel

# Specify custom output directory
uv build --out-dir dist/
```

### 2. Pre-Release Lockfile Synchronization
Ensure all dependencies are synchronized and locked against `pyproject.toml` before building:
```bash
# Verify environment conforms strictly to lockfile
uv sync --frozen
```

### 3. Publishing to PyPI
Publish compiled artifacts using native `uv publish` or standard `twine`:

```bash
# Publish using uv native publishing
uv publish

# Or publish to TestPyPI
uv publish --publish-url https://test.pypi.org/legacy/
```

---

## 🔗 Related Resources

- **Layer 1 Software Guides:**
  - [`software/uv/00-overview.md`](./00-overview.md) — UV overview and toolchain benchmarks.
  - [`software/uv/06-troubleshooting.md`](./06-troubleshooting.md) — UV lockfile and build troubleshooting.
  - [`software/cpython/03-workflows.md`](../cpython/03-workflows.md) — Standard CPython `build` and Twine workflows.
  - [`software/git/03-workflows.md`](../git/03-workflows.md) — Git release branching and tagging SOP.
- **Layer 2 Concepts & Workflows:**
  - [`concepts/version_control/03-release-tagging-and-changelogs.md`](../../concepts/version_control/03-release-tagging-and-changelogs.md) — Release lifecycle, SSOT versioning, and changelog theory.
  - [`workflows/11-python-package-git-release-workflow.md`](../../workflows/11-python-package-git-release-workflow.md) — Universal 12-step release pipeline SOP.
  - [`cheat_sheets/python-packaging-cheat-sheet.md`](../../cheat_sheets/python-packaging-cheat-sheet.md) — Python packaging quick reference.
- **Layer 3 Active Learning & Research:**
  - [`active_learning/research/git-release-workflow-for-sdxpy.md`](../../active_learning/research/git-release-workflow-for-sdxpy.md) — Master research document and ADR.

---

**Tags:** #software #uv #workflows #packaging #build #publish #pypi #wheels #sdist #lockfile

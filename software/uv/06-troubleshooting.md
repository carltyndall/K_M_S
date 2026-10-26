# uv Troubleshooting

## Common Issues
- **Issue:** Lockfile conflicts after manual `pyproject.toml` changes.
  - **Solution:** Run `uv lock` to regenerate the lockfile or `uv sync` to attempt a merge and sync.
- **Issue:** Environment not reflecting recent changes.
  - **Solution:** Force a re-sync with `uv sync --reinstall`.

- **Issue: `uv build` fails or omits package submodules in wheel.**
  - **Root Cause:** The `[build-system]` table is missing from `pyproject.toml` or module folders omit `__init__.py`.
  - **Solution:** Specify the PEP 517 build backend in `pyproject.toml`:
    ```toml
    [build-system]
    requires = ["setuptools>=61.0", "wheel"]
    build-backend = "setuptools.build_meta"
    ```
    Ensure all module subdirectories contain `__init__.py` and inspect compiled wheel contents:
    ```bash
    python -m zipfile -l dist/*.whl
    ```

- **Issue: `uv sync --frozen` rejects release build in CI/CD.**
  - **Root Cause:** Dependencies in `pyproject.toml` changed without regenerating `uv.lock`.
  - **Solution:** Run `uv lock` locally to update the lockfile, commit `uv.lock`, and rerun the build.

---

## 🔗 Related Resources

- **Layer 1 Software Guides:**
  - [`software/uv/03-workflows.md`](./03-workflows.md) — UV workspace management, `uv build`, and packaging SOP.
  - [`software/cpython/06-troubleshooting.md`](../cpython/06-troubleshooting.md) — CPython and Twine distribution troubleshooting.
- **Layer 2 Concepts & Workflows:**
  - [`concepts/version_control/03-release-tagging-and-changelogs.md`](../../concepts/version_control/03-release-tagging-and-changelogs.md) — Release lifecycle, SSOT versioning, and changelog theory.
  - [`workflows/11-python-package-git-release-workflow.md`](../../workflows/11-python-package-git-release-workflow.md) — Universal 12-step release pipeline SOP.
  - [`cheat_sheets/python-packaging-cheat-sheet.md`](../../cheat_sheets/python-packaging-cheat-sheet.md) — Python packaging quick reference.
- **Layer 3 Active Learning & Research:**
  - [`active_learning/research/git-release-workflow-for-sdxpy.md`](../../active_learning/research/git-release-workflow-for-sdxpy.md) — Master research document and ADR.

---

**Tags:** #software #uv #troubleshooting #packaging #build #lockfile #pypi #wheels

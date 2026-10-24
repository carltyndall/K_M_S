# Naming Conventions & File Hygiene

Consistency across file and directory names simplifies navigation and scripting.

---

## 🏷️ Standards

| Element | Format | Example | Rationale |
| :--- | :--- | :--- | :--- |
| **Directories** | `snake_case` | `active_learning/`, `daily_notes/` | Terminal friendly, aligns with PEP 8 |
| **Markdown Files** | `numeric-prefix + kebab-case` | `01-setup-guide.md` | Enforces sequential ordering |
| **Jupyter Notebooks** | `numeric-prefix + snake_case` | `01_setup_guide.ipynb` | Importable as valid Python identifiers |

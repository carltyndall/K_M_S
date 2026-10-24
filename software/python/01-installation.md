# Python: Installation & Setup

Guide to installing and verifying the Python runtime.

## 📥 Installation Steps (Windows 11)
1. Download Python 3.12+ from [python.org](https://www.python.org/) or install via `winget`:
   ```powershell
   winget install Python.Python.3.12
   ```
2. Verify that Python is available in PowerShell:
   ```powershell
   python --version
   ```

## 🔍 Verification Checklist
- [ ] `python --version` returns version 3.12 or higher.
- [ ] Interactive REPL starts when typing `python`.
- [ ] Exiting the REPL works using `exit()` or `Ctrl + Z` then Enter.

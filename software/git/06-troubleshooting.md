# Git: Troubleshooting Log

Solutions to common Git errors.

---

### Issue: `fatal: not a git repository`
- **Cause:** Command run outside of an initialized Git folder.
- **Fix:** Navigate to repo root or run `git init`.

---

### Issue: Accidentally staged unwanted file
- **Fix:** Unstage using `git restore --staged <file>`.

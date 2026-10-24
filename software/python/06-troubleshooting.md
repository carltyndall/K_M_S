# Python: Troubleshooting Log

Curated record of common errors, root cause explanations, and verified fixes.

---

### Issue: `SyntaxError: invalid syntax`
- **Cause:** Missing colon (`:`), unclosed parentheses, or misspelled keywords.
- **Fix:** Check line and column numbers reported in traceback; verify quotes and brackets are paired.

---

### Issue: `IndentationError: unexpected indent`
- **Cause:** Mixing tabs and spaces or misaligned indentation blocks.
- **Fix:** Standardize on 4 spaces per indentation level.

---

### Issue: `NameError: name 'x' is not defined`
- **Cause:** Referencing a variable before assigning a value or variable is outside scope.
- **Fix:** Ensure the variable is assigned prior to use and spelled correctly.

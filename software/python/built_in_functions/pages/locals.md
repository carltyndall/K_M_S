# locals

Return a mapping of names in the current local scope.

**Signature:** `locals()`

Mutating the returned mapping is not a portable way to change local variables; behavior depends on scope and Python version.

```python
x = 3
'x' in locals()  # True
```

[Runnable locals MWE](../../05-projects/locals_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#locals)

# sentinel

Create a unique, truthy sentinel object, normally compared by identity.

**Signature:** `sentinel(name, /, *, repr=None)`

Added in Python 3.15.

```python
MISSING = sentinel('MISSING')
value = MISSING
value is MISSING  # True
```

[Runnable sentinel MWE](../../05-projects/sentinel_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#sentinel)

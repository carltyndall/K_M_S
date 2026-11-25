# getattr

Retrieve a named attribute, returning the optional default if it is absent.

**Signature:** `getattr(object, name, /)` or `getattr(object, name, default, /)`

Without a default, a missing attribute raises `AttributeError`.

```python
getattr('hello', 'missing', None)  # None
```

[Runnable getattr MWE](../../05-projects/getattr_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#getattr)

# ImportError

Raised when an import fails, including when a requested name cannot be found. `name` and `path` may provide context; [`ModuleNotFoundError`](ModuleNotFoundError.md) is a subclass.

```python
try:
    from math import nonexistent_name
except ImportError as exc:
    print(exc)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ImportError)
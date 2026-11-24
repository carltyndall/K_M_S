# ImportCycleError

An [`ImportError`](ImportError.md) raised when a lazy import directly or indirectly tries to import itself. Added in Python 3.15.

```python
# In Python 3.15+, handle a lazy import cycle specifically:
try:
    raise ImportCycleError('lazy import cycle')
except ImportError as exc:
    print(exc)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ImportCycleError)
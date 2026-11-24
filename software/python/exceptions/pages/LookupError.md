# LookupError

Base class for invalid mapping keys and sequence indexes, including [`KeyError`](KeyError.md) and [`IndexError`](IndexError.md).

```python
try:
    [][0]
except LookupError as exc:
    print(type(exc).__name__)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#LookupError)
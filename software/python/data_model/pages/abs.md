# `__abs__`

`__abs__(self)` implements absolute value for `abs(x)`.

```python
class Value:
    def __abs__(self): return 42

x = Value()
assert abs(x) == 42
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__abs__) and the [grouped index](../01-grouped-index.md).

# `__invert__`

`__invert__(self)` implements bitwise inversion for `~x`.

```python
class Value:
    def __invert__(self): return 42

x = Value()
assert ~x == 42
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__invert__) and the [grouped index](../01-grouped-index.md).

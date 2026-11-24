# `__neg__`

`__neg__(self)` implements negation for `-x`.

```python
class Value:
    def __neg__(self): return 42

x = Value()
assert -x == 42
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__neg__) and the [grouped index](../01-grouped-index.md).

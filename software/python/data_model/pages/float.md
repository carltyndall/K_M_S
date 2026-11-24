# `__float__`

`__float__(self)` supplies the float returned by `float(x)`.

```python
class Value:
    def __float__(self): return 2.0

x = Value()
assert float(x) == 2.0
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__float__) and the [grouped index](../01-grouped-index.md).

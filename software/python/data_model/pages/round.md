# `__round__`

`__round__(self, ndigits=None)` implements `round(x)` and `round(x, ndigits)`; the optional argument controls precision.

```python
class Value:
    def __round__(self, ndigits=None): return ndigits if ndigits is not None else 0

assert round(Value(), 2) == 2
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__round__) and the [grouped index](../01-grouped-index.md).

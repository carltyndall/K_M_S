# `__length_hint__`

`__length_hint__(self)` offers an estimated non-negative length for optimization; it is not required to be accurate and may return `NotImplemented`.

```python
import operator

class Value:
    def __length_hint__(self): return 3

assert operator.length_hint(Value()) == 3
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__length_hint__) and the [grouped index](../01-grouped-index.md).

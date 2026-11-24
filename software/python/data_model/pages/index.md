# `__index__`

`__index__(self)` supplies the exact integer returned by `operator.index(x)`. It must return an `int` and also enables integer-only operations such as slicing.

```python
import operator

class Value:
    def __index__(self): return 2

x = Value()
assert operator.index(x) == 2
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__index__) and the [grouped index](../01-grouped-index.md).

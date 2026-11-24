# `__ceil__`

`__ceil__(self)` supplies the ceiling integral value returned by `math.ceil(x)`.

```python
import math

class Value:
    def __ceil__(self): return 2

x = Value()
assert math.ceil(x) == 2
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__ceil__) and the [grouped index](../01-grouped-index.md).

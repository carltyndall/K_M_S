# `__floor__`

`__floor__(self)` supplies the floor integral value returned by `math.floor(x)`.

```python
import math

class Value:
    def __floor__(self): return 2

x = Value()
assert math.floor(x) == 2
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__floor__) and the [grouped index](../01-grouped-index.md).

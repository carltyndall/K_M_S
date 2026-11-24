# `__trunc__`

`__trunc__(self)` supplies the truncated integral value returned by `math.trunc(x)`.

```python
import math

class Value:
    def __trunc__(self): return 2

x = Value()
assert math.trunc(x) == 2
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__trunc__) and the [grouped index](../01-grouped-index.md).

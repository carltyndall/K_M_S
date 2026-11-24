# `__ne__`

`__ne__(self, other)` implements `!=` (not equal to). Return `NotImplemented` for unsupported operand types so Python can try the reflected comparison; comparison results need not be Boolean.

```python
class Number:
    def __ne__(self, other):
        if not isinstance(other, Number): return NotImplemented
        return 1 != 2

assert (Number() != Number()) is True
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__ne__) and the [grouped index](../01-grouped-index.md).

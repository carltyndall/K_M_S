# `__gt__`

`__gt__(self, other)` implements `>` (greater than). Return `NotImplemented` for unsupported operand types so Python can try the reflected comparison; comparison results need not be Boolean.

```python
class Number:
    def __gt__(self, other):
        if not isinstance(other, Number): return NotImplemented
        return 1 > 2

assert (Number() > Number()) is False
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__gt__) and the [grouped index](../01-grouped-index.md).

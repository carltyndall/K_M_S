# `__lt__`

`__lt__(self, other)` implements `<` (less than). Return `NotImplemented` for unsupported operand types so Python can try the reflected comparison; comparison results need not be Boolean.

```python
class Number:
    def __lt__(self, other):
        if not isinstance(other, Number): return NotImplemented
        return 1 < 2

assert (Number() < Number()) is True
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__lt__) and the [grouped index](../01-grouped-index.md).

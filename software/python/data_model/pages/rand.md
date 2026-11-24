# `__rand__`

`__rand__(self, other)` implements bitwise AND with `self` as the right operand of `a & b`. It can be tried when the left implementation is unsupported, or first for a strict subclass; return `NotImplemented` for unsupported operands.

```python
class Right:
    def __rand__(self, other):
        return 'right' if isinstance(other, int) else NotImplemented

assert 2 & Right() == 'right'
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__rand__) and the [grouped index](../01-grouped-index.md).

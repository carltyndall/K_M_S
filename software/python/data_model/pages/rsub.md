# `__rsub__`

`__rsub__(self, other)` implements subtraction with `self` as the right operand of `a - b`. It can be tried when the left implementation is unsupported, or first for a strict subclass; return `NotImplemented` for unsupported operands.

```python
class Right:
    def __rsub__(self, other):
        return 'right' if isinstance(other, int) else NotImplemented

assert 2 - Right() == 'right'
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__rsub__) and the [grouped index](../01-grouped-index.md).

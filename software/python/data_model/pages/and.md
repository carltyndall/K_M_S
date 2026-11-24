# `__and__`

`__and__(self, other)` implements bitwise AND for `a & b`. Return `NotImplemented` for unsupported operands; Python may then try the right operand's reflected method, which can take priority when its type is a strict subclass.

```python
class Left:
    def __and__(self, other):
        return 'left' if isinstance(other, int) else NotImplemented

assert Left() & 2 == 'left'
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__and__) and the [grouped index](../01-grouped-index.md).

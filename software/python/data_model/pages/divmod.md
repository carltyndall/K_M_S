# `__divmod__`

`__divmod__(self, other)` implements quotient and remainder for `divmod(a, b)`. Return `NotImplemented` for unsupported operands; Python may then try the right operand's reflected method, which can take priority when its type is a strict subclass.

```python
class Left:
    def __divmod__(self, other):
        return 'left' if isinstance(other, int) else NotImplemented

assert divmod(Left(), 2) == 'left'
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__divmod__) and the [grouped index](../01-grouped-index.md).

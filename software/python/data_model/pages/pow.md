# `__pow__`

`__pow__(self, other, modulo=None)` implements exponentiation for `a ** b` and `pow(a, b, modulo)`. The optional third argument supports modular exponentiation. Return `NotImplemented` for unsupported operands; Python may then try [`__rpow__`](rpow.md), which can take priority when its type is a strict subclass. See [`NotImplemented`](../../built_in_types/pages/notimplemented.md).

```python
class Left:
    def __pow__(self, other):
        return 'left' if isinstance(other, int) else NotImplemented

assert Left() ** 2 == 'left'
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__pow__) and the [grouped index](../01-grouped-index.md).

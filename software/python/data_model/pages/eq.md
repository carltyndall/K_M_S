# `__eq__`

`__eq__(self, other)` implements `==`. Return `NotImplemented` for unsupported operands so Python can try the other operand's comparison; it is not the same as raising `NotImplementedError`. If neither handles equality, Python falls back to identity.

```python
class Point:
    def __init__(self, x): self.x = x
    def __eq__(self, other):
        if not isinstance(other, Point): return NotImplemented
        return self.x == other.x

assert Point(1) == Point(1)
```

See [`__hash__`](hash.md), [`NotImplemented`](../../built_in_types/pages/notimplemented.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__lt__).
# `__add__`

`__add__(self, other)` implements `self + other`. Return `NotImplemented` for unsupported types. Python can try the right operand's `__radd__`; a strict subclass's reflected implementation can take precedence. `__iadd__` implements `+=`, falling back to ordinary addition when unavailable or returning `NotImplemented`.

```python
class Amount:
    def __init__(self, n): self.n = n
    def __add__(self, other):
        if not isinstance(other, Amount): return NotImplemented
        return Amount(self.n + other.n)

assert (Amount(1) + Amount(2)).n == 3
```

See [`NotImplemented`](../../built_in_types/pages/notimplemented.md) and [numeric emulation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) for other operators.
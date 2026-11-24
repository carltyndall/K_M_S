# `__len__`

`__len__(self)` returns a non-negative integer length. It supports `len()` and, absent `__bool__`, truth testing.

```python
class Box:
    def __len__(self): return 3

assert len(Box()) == 3
```

See [`__bool__`](bool.md), [sequence operations](../../built_in_types/pages/sequence_operations.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__len__).
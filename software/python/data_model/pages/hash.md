# `__hash__`

`__hash__(self)` returns an integer for hash-based collections. Equal objects must have equal hashes, and a key's hash must remain stable while stored. Defining `__eq__` without `__hash__` normally makes instances unhashable.

```python
class Key:
    def __init__(self, value): self.value = value
    def __eq__(self, other):
        return self.value == other.value if isinstance(other, Key) else NotImplemented
    def __hash__(self): return hash(self.value)

assert Key('a') in {Key('a')}
```

Treat `value` as immutable once used as a key. See [`__eq__`](eq.md), [`dict`](../../built_in_types/pages/dict.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__hash__).
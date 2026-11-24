# `__getitem__`

`__getitem__(self, key)` implements subscription. Sequence implementations should support integer indices and raise `IndexError` when out of range; mappings use keys and normally raise `KeyError` for missing keys. Slice syntax passes a `slice` object.

```python
class Items:
    def __getitem__(self, key): return [10, 20, 30][key]

assert Items()[1:] == [20, 30]
```

See [`__iter__`](iter.md), [`__setitem__`](setitem.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__getitem__).
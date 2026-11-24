# `__delitem__`

`__delitem__(self, key)` implements `del obj[key]`. Raise `KeyError` for a missing mapping key or `IndexError` for an invalid sequence index.

```python
class Box:
    def __init__(self): self.data = {'a': 1}
    def __delitem__(self, key): del self.data[key]

x = Box()
del x['a']
assert not x.data
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__delitem__) and the [grouped index](../01-grouped-index.md).

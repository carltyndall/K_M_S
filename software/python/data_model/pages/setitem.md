# `__setitem__` and `__delitem__`

`__setitem__(self, key, value)` implements subscription assignment; `__delitem__(self, key)` implements subscription deletion. Appropriate errors depend on whether the object behaves as a sequence or mapping.

```python
class Store:
    def __init__(self): self.data = {}
    def __setitem__(self, key, value): self.data[key] = value
    def __delitem__(self, key): del self.data[key]

s = Store()
s['x'] = 1
del s['x']
assert not s.data
```

See [`__getitem__`](getitem.md), [`del`](../../keywords/pages/del.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__setitem__).
# `__missing__`

`__missing__(self, key)` is called by `dict.__getitem__` for a missing key on a `dict` subclass; methods such as `get` do not invoke it.

```python
class Defaults(dict):
    def __missing__(self, key): return 0

assert Defaults()['absent'] == 0
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__missing__) and the [grouped index](../01-grouped-index.md).

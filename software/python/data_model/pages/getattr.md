# `__getattr__`

`__getattr__(self, name)` is called when normal attribute lookup fails with `AttributeError`. Return a fallback value or raise `AttributeError` for an unknown name.

```python
class Defaults:
    def __getattr__(self, name):
        if name == 'colour': return 'blue'
        raise AttributeError(name)

assert Defaults().colour == 'blue'
```

See [`__getattribute__`](getattribute.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__getattr__).
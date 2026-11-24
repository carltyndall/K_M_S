# `__irshift__`

`__irshift__(self, other)` implements `a >>= b`. It may mutate `self` or return a replacement. If absent or it returns `NotImplemented`, Python falls back to the ordinary and reflected operations.

```python
class Value:
    def __irshift__(self, other):
        return other

x = Value()
x >>= 2
assert x == 2
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__irshift__) and the [grouped index](../01-grouped-index.md).

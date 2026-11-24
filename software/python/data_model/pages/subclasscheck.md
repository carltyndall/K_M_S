# `__subclasscheck__`

`__subclasscheck__(cls, subclass)` customizes `issubclass(subclass, cls)` when defined on the metaclass of `cls`.

```python
class Meta(type):
    def __subclasscheck__(cls, subclass): return subclass is int

class C(metaclass=Meta): pass

assert issubclass(int, C)
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#type.__subclasscheck__) and the [grouped index](../01-grouped-index.md).

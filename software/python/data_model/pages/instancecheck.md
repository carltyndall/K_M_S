# `__instancecheck__`

`__instancecheck__(cls, instance)` customizes `isinstance(instance, cls)` when defined on the metaclass of `cls`.

```python
class Meta(type):
    def __instancecheck__(cls, instance): return isinstance(instance, int)

class C(metaclass=Meta): pass

assert isinstance(3, C)
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#type.__instancecheck__) and the [grouped index](../01-grouped-index.md).

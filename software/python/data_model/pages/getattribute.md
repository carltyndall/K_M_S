# `__getattribute__`

`__getattribute__(self, name)` handles every ordinary instance attribute read. Delegate to `object.__getattribute__` to avoid infinite recursion; `__getattr__` can run if it raises `AttributeError`. Implicit special method lookup may bypass this hook.

```python
class Logged:
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

assert Logged().__class__ is Logged
```

See [special method lookup](special_method_lookup.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__).
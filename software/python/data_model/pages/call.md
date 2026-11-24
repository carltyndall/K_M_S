# `__call__`

`__call__(self, ...)` lets an instance be called like a function. Arguments are passed to the method after `self`.

```python
class Scale:
    def __call__(self, x): return x * 2

assert Scale()(3) == 6
```

See [functions](../../built_in_types/pages/functions.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__call__).
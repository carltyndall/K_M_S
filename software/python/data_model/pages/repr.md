# `__repr__`

`__repr__(self)` returns a string intended as an informative, unambiguous representation. When practical it resembles an expression that could recreate the object. If `__str__` is absent, `str()` can fall back to it.

```python
class Point:
    def __repr__(self):
        return 'Point(3)'

assert repr(Point()) == 'Point(3)'
```

See [`__str__`](str.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__repr__).
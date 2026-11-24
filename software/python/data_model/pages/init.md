# `__init__`

`__init__(self, ...)` initializes an instance created by `__new__`. It must return `None`; it does not create the object itself.

```python
class Point:
    def __init__(self, x):
        self.x = x

assert Point(3).x == 3
```

See [`__new__`](new.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__init__).
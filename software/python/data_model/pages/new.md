# `__new__`

`__new__(cls, ...)` creates an instance before initialization. It is especially useful for immutable subclasses. If it returns an instance of `cls`, Python calls `__init__`; otherwise initialization is skipped.

```python
class Positive(int):
    def __new__(cls, value):
        return super().__new__(cls, abs(value))

assert Positive(-3) == 3
```

See [`__init__`](init.md), [`int`](../../built_in_types/pages/int.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__new__).
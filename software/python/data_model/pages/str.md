# `__str__`

`__str__(self)` returns the informal, readable string used by `str()` and `print()`. It must return a string.

```python
class Greeting:
    def __str__(self):
        return 'hello'

assert str(Greeting()) == 'hello'
```

See [`__repr__`](repr.md), [`str`](../../built_in_types/pages/str.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__str__).
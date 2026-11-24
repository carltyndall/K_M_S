# `__bool__`

`__bool__(self)` implements truth testing and must return a `bool`. Without it, Python uses `__len__`; without either method an instance is true by default.

```python
class Switch:
    def __bool__(self): return False

assert not Switch()
```

See [truth value testing](../../built_in_types/pages/truth_value_testing.md), [`__len__`](len.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__bool__).
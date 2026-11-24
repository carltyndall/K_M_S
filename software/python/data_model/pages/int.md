# `__int__`

`__int__(self)` supplies the integer returned by `int(x)`.

```python
class Value:
    def __int__(self): return 2

x = Value()
assert int(x) == 2
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__int__) and the [grouped index](../01-grouped-index.md).

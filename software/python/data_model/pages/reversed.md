# `__reversed__`

`__reversed__(self)` implements `reversed(x)` and should return a reverse iterator. Without it, `reversed` can fall back to the sequence protocol.

```python
class Value:
    def __reversed__(self): return iter([2, 1])

assert list(reversed(Value())) == [2, 1]
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__reversed__) and the [grouped index](../01-grouped-index.md).

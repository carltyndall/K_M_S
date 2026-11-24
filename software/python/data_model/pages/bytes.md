# `__bytes__`

`__bytes__(self)` implements `bytes(x)` and must return a `bytes` object.

```python
class Value:
    def __bytes__(self): return b'value'

assert bytes(Value()) == b'value'
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__bytes__) and the [grouped index](../01-grouped-index.md).

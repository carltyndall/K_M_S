# `__dir__`

`__dir__(self)` supplies names for `dir(x)`; `dir` sorts the returned iterable.

```python
class Value:
    def __dir__(self): return ['z', 'a']

assert dir(Value()) == ['a', 'z']
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__dir__) and the [grouped index](../01-grouped-index.md).

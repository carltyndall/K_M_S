# `__pos__`

`__pos__(self)` implements unary plus for `+x`.

```python
class Value:
    def __pos__(self): return 42

x = Value()
assert +x == 42
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__pos__) and the [grouped index](../01-grouped-index.md).

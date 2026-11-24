# `__complex__`

`__complex__(self)` supplies the complex number returned by `complex(x)`.

```python
class Value:
    def __complex__(self): return 2j

x = Value()
assert complex(x) == 2j
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__complex__) and the [grouped index](../01-grouped-index.md).

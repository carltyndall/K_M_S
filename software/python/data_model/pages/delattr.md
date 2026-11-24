# `__delattr__`

`__delattr__(self, name)` handles `del obj.name`. Use `object.__delattr__` to perform the default deletion without recursion.

```python
class Value:
    def __delattr__(self, name): object.__delattr__(self, name)

x = Value()
x.a = 1
del x.a
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__delattr__) and the [grouped index](../01-grouped-index.md).

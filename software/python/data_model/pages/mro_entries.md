# `__mro_entries__`

`__mro_entries__(self, bases)` replaces a non-type base in a class statement with a tuple of types before the metaclass is selected.

```python
class Substitute:
    def __mro_entries__(self, bases): return (dict,)

class C(Substitute()): pass

assert C.__bases__ == (dict,)
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__mro_entries__) and the [grouped index](../01-grouped-index.md).

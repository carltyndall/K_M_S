# `__exit__`

`__exit__(self, exc_type, exc_value, traceback)` runs when a `with` block exits. A truthy return suppresses an exception; on normal exit all three arguments are `None`.

```python
class Context:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_value, traceback): return exc_type is ValueError

with Context():
    raise ValueError('suppressed')
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__exit__) and the [grouped index](../01-grouped-index.md).

# `__enter__` and `__exit__`

`__enter__(self)` acquires a context and returns the value bound by `as`. `__exit__(self, exc_type, exc_value, traceback)` performs cleanup; arguments are `None` on normal exit. A truthy return suppresses an exception; otherwise it propagates.

```python
class Context:
    def __enter__(self): return 'ready'
    def __exit__(self, exc_type, exc_value, traceback): return False

with Context() as value:
    assert value == 'ready'
```

See [`with`](../../keywords/pages/with.md), [context managers](../../built_in_types/pages/context_managers.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#context-managers).
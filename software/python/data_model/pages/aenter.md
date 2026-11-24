# `__aenter__` and `__aexit__`

Asynchronous context managers provide awaitables from `__aenter__` and `__aexit__`. Like synchronous `__exit__`, a truthy exit result suppresses an exception. Use `async with` inside asynchronous code.

```python
class AsyncContext:
    async def __aenter__(self): return 'ready'
    async def __aexit__(self, exc_type, exc_value, traceback): return False

async def use():
    async with AsyncContext() as value:
        assert value == 'ready'
```

See [`__enter__` and `__exit__`](enter.md), [`async`](../../keywords/pages/async.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#asynchronous-context-managers).
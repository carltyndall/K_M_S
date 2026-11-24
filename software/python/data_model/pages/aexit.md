# `__aexit__`

`__aexit__(self, exc_type, exc_value, traceback)` returns an awaitable used on exit from `async with`. Its truthy result suppresses an exception.

```python
class Context:
    async def __aenter__(self): return self
    async def __aexit__(self, exc_type, exc_value, traceback): return exc_type is ValueError

async def example():
    async with Context():
        raise ValueError('suppressed')
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__aexit__) and the [grouped index](../01-grouped-index.md).

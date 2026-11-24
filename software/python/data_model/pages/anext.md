# `__anext__`

`__anext__(self)` returns an awaitable yielding the next asynchronous item, or raising `StopAsyncIteration` when exhausted.

```python
class Empty:
    def __aiter__(self): return self
    async def __anext__(self): raise StopAsyncIteration

async def example():
    return [item async for item in Empty()]  # []
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__anext__) and the [grouped index](../01-grouped-index.md).

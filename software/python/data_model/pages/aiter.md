# `__aiter__` and `__anext__`

`__aiter__(self)` returns an asynchronous iterator directly. `__anext__(self)` returns an awaitable that produces the next value or raises `StopAsyncIteration` when exhausted.

```python
class Countdown:
    def __init__(self): self.n = 2
    def __aiter__(self): return self
    async def __anext__(self):
        if not self.n: raise StopAsyncIteration
        self.n -= 1
        return self.n

async def collect():
    return [x async for x in Countdown()]  # [1, 0]
```

See [`async`](../../keywords/pages/async.md), [asynchronous generators](../../built_in_types/pages/async_generators.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#asynchronous-iterators).
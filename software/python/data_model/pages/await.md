# `__await__`

`__await__(self)` must return an iterator used by `await`. What the iterator yields is interpreted by the asynchronous framework; normally delegate to an existing awaitable rather than inventing a scheduler protocol.

```python
class Deferred:
    def __await__(self):
        async def result(): return 42
        return result().__await__()

async def use():
    assert await Deferred() == 42
```

See [`await`](../../keywords/pages/await.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__await__).
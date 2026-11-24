# StopAsyncIteration

Signals exhaustion from an asynchronous iterator's `__anext__` method; it is handled by `async for`.

```python
class Empty:
    def __aiter__(self):
        return self
    async def __anext__(self):
        raise StopAsyncIteration
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#StopAsyncIteration)
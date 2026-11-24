# Asynchronous generator iterators

An `async def` function containing `yield` creates an asynchronous generator iterator. Consume it with `async for` or await its `__anext__()`; it also provides `asend()`, `athrow()` and `aclose()`.

```python
async def values():
    yield 1
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#asynchronous-generator-iterators)
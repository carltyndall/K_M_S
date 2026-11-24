# Await expressions

An await expression suspends a coroutine until an awaitable completes and produces its result. It is valid in an asynchronous function, not an ordinary synchronous function.

```python
async def length():
    return len(await get_text())
```

See [`await`](../../keywords/pages/await.md) and [coroutines](../../statements/pages/coroutines.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#await-expression)
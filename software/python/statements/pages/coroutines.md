# Coroutines

Calling an `async def` function produces a coroutine object; it must be awaited or scheduled to execute. `async for` and `async with` use asynchronous iteration and context management inside asynchronous functions.

```python
async def answer():
    return 42

async def main():
    return await answer()
```

See [`async`](../../keywords/pages/async.md) and [await expressions](../../expressions/pages/await-expressions.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#coroutines)
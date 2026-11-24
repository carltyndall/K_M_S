# await

`await` suspends a coroutine until an awaitable completes and produces its result. It is used in asynchronous functions.

```python
async def greet():
    return 'hello'

async def message():
    return await greet()
```

`await` became a reserved keyword in Python 3.7; it was introduced in 3.5.

[Python documentation](https://docs.python.org/3/reference/expressions.html#await-expression)
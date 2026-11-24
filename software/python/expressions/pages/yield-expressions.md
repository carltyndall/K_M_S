# Yield expressions

`yield` suspends a generator and can receive a value when resumed with `send`. `yield from` delegates to a subiterator and evaluates to its return value. Parentheses are required in some expression contexts.

```python
def numbers():
    yield from (1, 2)

list(numbers())  # [1, 2]
```

See [`yield`](../../keywords/pages/yield.md) and [generators](../../built_in_types/pages/generators.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#yield-expressions)
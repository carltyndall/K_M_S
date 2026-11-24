# yield

`yield` produces a value from a generator and suspends it until resumed. `yield from` delegates to another iterable or generator.

```python
def numbers():
    yield 1
    yield 2

list(numbers())  # [1, 2]
```

[Python documentation](https://docs.python.org/3/reference/expressions.html#yield-expressions)
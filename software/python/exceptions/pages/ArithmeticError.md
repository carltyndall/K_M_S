# ArithmeticError

Base class for arithmetic failures such as [`ZeroDivisionError`](ZeroDivisionError.md) and [`OverflowError`](OverflowError.md).

```python
try:
    1 / 0
except ArithmeticError as exc:
    print(type(exc).__name__)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ArithmeticError)
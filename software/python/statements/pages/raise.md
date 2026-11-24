# Raise statement

Raise an exception instance or exception class; a bare raise re-raises the active exception. `raise ... from ...` sets an explicit cause, and `from None` suppresses display of the implicit context.

```python
try:
    int('bad')
except ValueError as exc:
    raise RuntimeError('invalid input') from exc
```

See [`raise`](../../keywords/pages/raise.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)
# Try statement

Handlers select exceptions raised in the `try` suite. `else` runs only after a normal suite completion; `finally` runs during cleanup, including on return or exception. `except*` handles matching parts of exception groups and cannot be mixed with ordinary `except` in the same statement.

```python
try:
    value = int('42')
except ValueError:
    value = 0
finally:
    print('done')
```

See [`try`](../../keywords/pages/try.md), [`except`](../../keywords/pages/except.md) and [`finally`](../../keywords/pages/finally.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
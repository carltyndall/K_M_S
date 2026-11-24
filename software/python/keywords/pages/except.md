# except

`except` handles matching exceptions raised by the associated `try` suite. `except*`, added in Python 3.11, handles matching subgroups of exception groups.

```python
try:
    number = int('no')
except ValueError:
    number = 0
```

[Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
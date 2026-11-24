# try

`try` groups code with exception handlers and/or cleanup code. Optional `else` runs if the try suite completes without an exception.

```python
try:
    number = int('42')
except ValueError:
    number = 0
```

[Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
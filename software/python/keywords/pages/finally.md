# finally

`finally` introduces cleanup code executed when leaving a `try` statement, whether or not an exception occurred.

```python
file = open('example.txt')
try:
    content = file.read()
finally:
    file.close()
```

[Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
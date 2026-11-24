# global

`global` declares that names assigned in the current code block refer to the module's global namespace.

```python
count = 0
def increment():
    global count
    count += 1
```

[Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)
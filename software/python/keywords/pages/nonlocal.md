# nonlocal

`nonlocal` declares that names refer to existing bindings in an enclosing function scope, allowing them to be rebound.

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

[Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement)
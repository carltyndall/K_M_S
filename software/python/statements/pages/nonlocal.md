# Nonlocal statement

The declaration directs binding to an existing name in the nearest enclosing function scope, rather than creating a local name. A missing enclosing binding is a syntax error.

```python
def counter():
    n = 0
    def increment():
        nonlocal n
        n += 1
        return n
    return increment
```

See [`nonlocal`](../../keywords/pages/nonlocal.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement)
# RecursionError

A [`RuntimeError`](RuntimeError.md) raised when the interpreter's maximum recursion depth is exceeded. Prefer fixing unbounded recursion over raising the limit blindly.

```python
def recurse():
    return recurse()

recurse()  # RecursionError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#RecursionError)
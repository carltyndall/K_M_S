# UnboundLocalError

A [`NameError`](NameError.md) raised when a local variable is referenced before it has a value.

```python
def f():
    print(value)
    value = 1  # assignment makes value local

f()  # UnboundLocalError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#UnboundLocalError)
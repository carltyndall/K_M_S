# Code objects

Code objects represent compiled executable Python code. Unlike function objects, they do not contain a reference to the global namespace or default argument values.

```python
def f(x):
    return x + 1
f.__code__.co_argcount  # 1
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#code-objects)
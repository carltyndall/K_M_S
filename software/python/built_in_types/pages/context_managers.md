# Context manager types

A context manager defines `__enter__()` and `__exit__()` for use with `with`. The exit method runs when the block leaves, including on exceptions, and can suppress an exception by returning a truthy value.

```python
with open('example.txt', encoding='utf-8') as file:
    text = file.read()
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#context-manager-types)
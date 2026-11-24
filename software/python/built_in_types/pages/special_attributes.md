# Special attributes

Many objects expose special read-only or writable attributes for introspection. The available attributes depend on the object type; for example, functions have `__name__` and `__code__`.

```python
def greet():
    pass
greet.__name__  # 'greet'
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#special-attributes)
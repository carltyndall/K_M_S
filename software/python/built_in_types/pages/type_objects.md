# Type objects

Type objects represent types and are usually callable to create instances. `type(obj)` returns an object's type; `isinstance()` also recognizes subclasses.

```python
type(1) is int  # True
isinstance(True, int)  # True
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#type-objects)
# Union type

The `|` operator between types creates a union type representing alternatives. A union can be used with `isinstance()` when its members are valid arguments to that function.

```python
isinstance('hello', int | str)  # True
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#union-type)
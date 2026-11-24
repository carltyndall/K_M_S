# Formatted string literals

An f-string evaluates replacement expressions at runtime and formats their values. Fields can include a debug `=`, a conversion such as `!r`, and a format specification.

```python
value = 3.14159
f'{value=:.2f}'  # 'value=3.14'
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#formatted-string-literals-f-strings)
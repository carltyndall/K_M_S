# Template string literals

Template string literals (`t`-strings) create `string.templatelib.Template` objects containing literal strings and evaluated interpolations, rather than immediately formatting a string. They were added in Python 3.14.

```python
name = 'Ada'
template = t'Hello, {name}!'
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#template-string-literals-t-strings)
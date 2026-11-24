# frozendict

`frozendict` is an immutable mapping added in Python 3.15. It is hashable when all its values are hashable, and can then be used as a dictionary key.

```python
settings = frozendict({'mode': 'fast'})
settings['mode']  # 'fast'
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#frozen-dictionaries)
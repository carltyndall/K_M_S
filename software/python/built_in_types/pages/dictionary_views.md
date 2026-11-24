# Dictionary view objects

`dict.keys()`, `dict.values()` and `dict.items()` return dynamic views reflecting changes to the dictionary. Keys views and suitably hashable items views support set operations.

```python
d = {'a': 1}
keys = d.keys()
d['b'] = 2
list(keys)  # ['a', 'b']
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#dictionary-view-objects)
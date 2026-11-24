# frozenset

`frozenset` is an immutable, hashable set of hashable objects. Unlike `set`, it can be used as a dictionary key or an element of another set.

```python
frozenset([1, 1, 2]) == frozenset({1, 2})  # True
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#set-types-set-frozenset)
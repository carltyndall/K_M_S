# Immutable sequence types

Immutable sequences cannot be changed in place. Hashable immutable sequences, such as tuples whose elements are all hashable, can serve as dictionary keys.

```python
{(1, 2): 'point'}[(1, 2)]  # 'point'
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#immutable-sequence-types)
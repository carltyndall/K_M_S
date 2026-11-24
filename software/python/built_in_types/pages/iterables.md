# Iterables

An iterable can provide an iterator, usually through `__iter__()`. Containers can generally be iterated repeatedly; an iterator itself may be exhausted after one pass.

```python
list(iter((1, 2)))  # [1, 2]
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#iterables)
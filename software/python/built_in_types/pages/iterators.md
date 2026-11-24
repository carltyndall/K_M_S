# Iterators

An iterator returns itself from `__iter__()` and produces successive values through `__next__()`. It raises `StopIteration` when exhausted and must remain exhausted thereafter.

```python
it = iter([1, 2])
next(it), next(it)  # (1, 2)
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#iterators)
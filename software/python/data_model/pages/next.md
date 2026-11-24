# `__next__`

`__next__(self)` returns the next item from an iterator or raises `StopIteration` when exhausted. An iterator's `__iter__` returns itself; once exhausted it must remain exhausted.

```python
it = iter([1])
assert next(it) == 1
assert next(it, 'end') == 'end'
```

See [`__iter__`](iter.md), [iterators](../../built_in_types/pages/iterators.md), and the [Python documentation](https://docs.python.org/3/library/stdtypes.html#iterator.__next__).
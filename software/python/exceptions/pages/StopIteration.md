# StopIteration

Signals that an iterator is exhausted. A generator's return value is available as `value`; an unexpected `StopIteration` escaping a generator is converted to `RuntimeError`.

```python
it = iter([1])
next(it)
next(it)  # StopIteration
```

See [iterators](../../built_in_types/pages/iterators.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#StopIteration)
# map

Return an iterator applying a function to items from one or more iterables.

**Signature:** `map(function, iterable, /, *iterables, strict=False)`

The `strict` option was added in Python 3.14; it raises `ValueError` for unequal iterable lengths.

```python
list(map(str, [1, 2]))  # ['1', '2']
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#map)

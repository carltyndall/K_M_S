# zip

Return an iterator of tuples containing corresponding items from each iterable.

**Signature:** `zip(*iterables, strict=False)`

`strict=True` raises `ValueError` for unequal lengths; it was added in Python 3.10.

```python
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]
```

[Runnable zip MWE](../../05-projects/zip_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#zip)

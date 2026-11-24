# Object lifetime

Objects can be garbage-collected when unreachable; collection timing and implementation vary. External resources should be closed explicitly, preferably with a context manager, rather than relying on finalization. Cycles can delay collection.

```python
with open('example.txt') as stream:
    text = stream.read()
```

See [`__del__`](del.md), [`__enter__` and `__exit__`](enter.md), [`with`](../../keywords/pages/with.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types).
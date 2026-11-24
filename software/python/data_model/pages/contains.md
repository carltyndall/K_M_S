# `__contains__`

`__contains__(self, item)` implements membership testing. Without it, Python tries iteration, then the old sequence protocol using `__getitem__`.

```python
class Even:
    def __contains__(self, n): return n % 2 == 0

assert 4 in Even()
```

See [`in`](../../keywords/pages/in.md), [`__iter__`](iter.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__contains__).
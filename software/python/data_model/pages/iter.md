# `__iter__`

`__iter__(self)` returns an iterator. Containers usually return a fresh iterator; an iterator returns itself. Without `__iter__`, iteration can fall back to integer `__getitem__` starting at zero until `IndexError`.

```python
class Bag:
    def __iter__(self): return iter((1, 2))

assert list(Bag()) == [1, 2]
```

See [`__next__`](next.md), [iterables](../../built_in_types/pages/iterables.md), [`for`](../../keywords/pages/for.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__iter__).
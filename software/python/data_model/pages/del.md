# `__del__`

`__del__(self)` is a finalizer, not the implementation of the `del` statement. It may run in precarious circumstances, including interpreter shutdown; exceptions are ignored and reported to standard error. It is not guaranteed to run for objects still alive at exit. Prefer explicit cleanup.

```python
class Resource:
    def close(self):
        pass  # release the resource explicitly
```

See [object lifetime](lifetime.md), [`del`](../../keywords/pages/del.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__del__).
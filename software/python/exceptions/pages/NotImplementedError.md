# NotImplementedError

A [`RuntimeError`](RuntimeError.md) commonly raised by abstract methods that subclasses must implement. It is not the same as the [`NotImplemented`](../../built_in_constants/pages/notimplemented.md) return value for unsupported operations.

```python
class Reader:
    def read(self):
        raise NotImplementedError('implement read()')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#NotImplementedError)
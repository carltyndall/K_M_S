# `__buffer__`

`__buffer__(self, flags)` returns a `memoryview` to export a buffer. The integer flags describe the consumer request. This Python-level hook was added in Python 3.12.

```python
class Buffer:
    def __buffer__(self, flags): return memoryview(b'abc')

assert bytes(memoryview(Buffer())) == b'abc'
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__buffer__) and the [grouped index](../01-grouped-index.md).

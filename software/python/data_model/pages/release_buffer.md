# `__release_buffer__`

`__release_buffer__(self, view)` is called when a buffer obtained through `__buffer__` is released. This Python-level hook was added in Python 3.12.

```python
class Buffer:
    def __init__(self): self.released = False
    def __buffer__(self, flags): return memoryview(b'abc')
    def __release_buffer__(self, view): self.released = True

x = Buffer()
v = memoryview(x)
v.release()
assert x.released
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__release_buffer__) and the [grouped index](../01-grouped-index.md).

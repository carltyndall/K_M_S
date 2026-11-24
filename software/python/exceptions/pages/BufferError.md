# BufferError

Raised when a buffer-related operation cannot be performed, for example resizing a buffer with an active export.

```python
data = bytearray(b'abc')
view = memoryview(data)
data.extend(b'd')  # BufferError while the view exists
```

See [`memoryview`](../../built_in_types/pages/memoryview.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#BufferError)
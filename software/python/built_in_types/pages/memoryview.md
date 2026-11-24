# memoryview

`memoryview` exposes a buffer from a supporting object without copying the underlying data. A writable view can modify a writable exporter; releasing the view releases its access to that buffer.

```python
data = bytearray(b'abc')
view = memoryview(data)
view[0] = 65  # data is now bytearray(b'Abc')
view.release()
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#memory-views)
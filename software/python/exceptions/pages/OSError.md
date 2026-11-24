# OSError

Base class for system-related failures. `errno`, `strerror`, `filename`, and `filename2` may describe the cause; `winerror` is Windows-specific. Construction with an OS error code may return a more specific subclass.

```python
try:
    open('/path/that/does/not/exist')
except OSError as exc:
    print(exc.errno, exc.filename)
```

See [`open`](../../built_in_functions/pages/open.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#OSError)
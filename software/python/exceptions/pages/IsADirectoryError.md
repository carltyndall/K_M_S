# IsADirectoryError

An [`OSError`](OSError.md) raised when a file operation is requested on a directory, corresponding to `EISDIR`.

```python
open('.', 'rb')  # IsADirectoryError on typical systems
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#IsADirectoryError)
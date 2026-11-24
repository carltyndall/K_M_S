# BrokenPipeError

A [`ConnectionError`](ConnectionError.md) raised when writing to a pipe or socket whose other end has closed, or when writing to a socket shut down for writing. Corresponds to `EPIPE` and `ESHUTDOWN`.

```python
try:
    raise BrokenPipeError('peer closed')
except ConnectionError:
    print('connection lost')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#BrokenPipeError)
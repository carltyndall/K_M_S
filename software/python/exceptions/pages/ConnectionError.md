# ConnectionError

An [`OSError`](OSError.md) base class for connection failures, including broken pipes, aborted, refused and reset connections.

```python
try:
    raise ConnectionResetError('peer reset connection')
except ConnectionError as exc:
    print(exc)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ConnectionError)
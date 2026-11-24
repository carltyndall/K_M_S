# ConnectionRefusedError

A [`ConnectionError`](ConnectionError.md) raised when a connection attempt is refused, corresponding to `ECONNREFUSED`.

```python
try:
    raise ConnectionRefusedError('connection refused')
except ConnectionError as exc:
    print(exc)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError)
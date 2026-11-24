# UnicodeDecodeError

A [`UnicodeError`](UnicodeError.md) raised when bytes cannot be decoded using the requested encoding.

```python
b'\xff'.decode('utf-8')  # UnicodeDecodeError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError)
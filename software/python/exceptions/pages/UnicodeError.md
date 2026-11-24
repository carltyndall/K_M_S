# UnicodeError

A [`ValueError`](ValueError.md) base class for encoding, decoding and translation failures. Attributes include `object`, `start`, `end`, `reason`, and `encoding` where applicable.

```python
try:
    b'\xff'.decode('utf-8')
except UnicodeError as exc:
    print(exc.start, exc.reason)
```

See [`str`](../../built_in_types/pages/str.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#UnicodeError)
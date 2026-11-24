# KeyError

A [`LookupError`](LookupError.md) raised when a mapping key is absent. Use `dict.get()` when a default is appropriate.

```python
settings = {'theme': 'dark'}
settings['language']  # KeyError
```

See [`dict`](../../built_in_types/pages/dict.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#KeyError)
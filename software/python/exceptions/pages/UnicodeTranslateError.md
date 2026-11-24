# UnicodeTranslateError

A [`UnicodeError`](UnicodeError.md) for a failure during Unicode translation. A custom translation handler can raise it explicitly.

```python
raise UnicodeTranslateError('abc', 0, 1, 'cannot translate')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#UnicodeTranslateError)
# TimeoutError

An [`OSError`](OSError.md) raised when a system operation times out, corresponding to `ETIMEDOUT`. Libraries may also define their own timeout exceptions.

```python
try:
    raise TimeoutError('operation timed out')
except TimeoutError:
    print('retry if appropriate')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#TimeoutError)
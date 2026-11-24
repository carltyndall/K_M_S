# ProcessLookupError

An [`OSError`](OSError.md) raised when a process does not exist, corresponding to `ESRCH`.

```python
import errno
raise ProcessLookupError(errno.ESRCH, 'no such process')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ProcessLookupError)
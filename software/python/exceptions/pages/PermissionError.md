# PermissionError

An [`OSError`](OSError.md) raised when access is denied, corresponding to `EACCES`, `EPERM`, and, on supported systems, `ENOTCAPABLE`.

```python
import errno
raise PermissionError(errno.EACCES, 'access denied', 'private.txt')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#PermissionError)
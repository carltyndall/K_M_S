# ChildProcessError

An [`OSError`](OSError.md) raised when an operation on a child process fails, corresponding to `ECHILD`.

```python
import errno
err = ChildProcessError(errno.ECHILD, 'no child process')
print(err.errno)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ChildProcessError)
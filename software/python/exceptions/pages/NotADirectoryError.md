# NotADirectoryError

An [`OSError`](OSError.md) raised when a directory operation is requested on a non-directory, corresponding to `ENOTDIR`.

```python
import errno
raise NotADirectoryError(errno.ENOTDIR, 'not a directory', 'file/child')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#NotADirectoryError)
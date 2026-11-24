# BlockingIOError

An [`OSError`](OSError.md) raised when a non-blocking operation would block. For buffered I/O, `characters_written` can report partial progress.

```python
import errno
err = BlockingIOError(errno.EAGAIN, 'try again later')
print(err.errno)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#BlockingIOError)
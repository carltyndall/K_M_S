# InterruptedError

An [`OSError`](OSError.md) associated with `EINTR`, when a system call is interrupted by a signal. Python retries many interrupted calls automatically unless the signal handler raises.

```python
import errno
err = InterruptedError(errno.EINTR, 'interrupted')
print(err.errno)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#InterruptedError)
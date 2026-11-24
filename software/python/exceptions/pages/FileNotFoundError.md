# FileNotFoundError

An [`OSError`](OSError.md) raised when a requested file or directory does not exist, corresponding to `ENOENT`.

```python
try:
    open('/path/that/does/not/exist')
except FileNotFoundError as exc:
    print(exc.filename)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#FileNotFoundError)
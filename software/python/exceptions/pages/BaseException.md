# BaseException

Root of the built-in exception hierarchy. Normally catch [`Exception`](Exception.md) instead: `BaseException` also includes termination signals. Instances expose `args`, traceback and chaining attributes; `add_note()` adds diagnostic context (3.11+).

```python
try:
    raise ValueError('invalid')
except Exception as exc:
    exc.add_note('while parsing input')
    raise
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#BaseException)
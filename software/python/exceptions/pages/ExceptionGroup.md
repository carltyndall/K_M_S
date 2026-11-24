# ExceptionGroup

A [`BaseExceptionGroup`](BaseExceptionGroup.md) and [`Exception`](Exception.md) subclass containing only `Exception` instances. Use `except*` to handle matching leaves independently. Added in Python 3.11.

```python
try:
    raise ExceptionGroup('batch', [ValueError('bad'), TypeError('wrong')])
except* ValueError as errors:
    print(errors)
except* TypeError as errors:
    print(errors)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ExceptionGroup)
# Exception

Base class for most application errors. Catch a more specific subclass when recovery depends on the cause; it does not catch `SystemExit` or `KeyboardInterrupt`.

```python
try:
    int('bad')
except Exception as exc:
    print(exc)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#Exception)
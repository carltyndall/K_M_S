# Generator types

Generator functions use `yield` to produce values lazily. Calling one creates a generator iterator, which resumes its suspended execution on each iteration and also supports `send()`, `throw()` and `close()`.

```python
def counts():
    yield 1
    yield 2
list(counts())  # [1, 2]
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#generator-types)
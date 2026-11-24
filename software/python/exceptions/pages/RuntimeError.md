# RuntimeError

Raised for an error that does not fit another category. More specific subclasses include [`RecursionError`](RecursionError.md) and [`NotImplementedError`](NotImplementedError.md).

```python
d = {'a': 1}
for key in d:
    d['b'] = 2  # RuntimeError: dictionary changed size
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#RuntimeError)
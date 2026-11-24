# MemoryError

Raised when an operation runs out of memory but the situation may still be recoverable. Recovery is not guaranteed.

```python
try:
    raise MemoryError('allocation failed')
except MemoryError:
    print('Reduce the workload')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#MemoryError)
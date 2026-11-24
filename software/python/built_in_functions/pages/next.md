# next

Retrieve the next item from an iterator, or the optional default when exhausted.

**Signature:** `next(iterator, /)` or `next(iterator, default, /)`

Without a default, exhaustion raises `StopIteration`.

```python
next(iter([]), 'done')  # 'done'
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#next)

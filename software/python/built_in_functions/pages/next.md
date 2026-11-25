# next

Retrieve the next item from an iterator, or the optional default when exhausted.

**Signature:** `next(iterator, /)` or `next(iterator, default, /)`

Without a default, exhaustion raises `StopIteration`.

```python
next(iter([]), 'done')  # 'done'
```

[Runnable next MWE](../../05-projects/next_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#next)

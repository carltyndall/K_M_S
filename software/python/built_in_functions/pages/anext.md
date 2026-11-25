# anext

Return an awaitable that retrieves the next item, or the optional default when exhausted.

**Signature:** `anext(async_iterator, /)` or `anext(async_iterator, default, /)`

Added in Python 3.10; without a default, exhaustion raises `StopAsyncIteration`.

```python
value = await anext(iterator, None)
```

[Runnable anext MWE](../../05-projects/anext_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#anext)

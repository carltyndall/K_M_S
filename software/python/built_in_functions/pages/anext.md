# anext

Return an awaitable that retrieves the next item, or the optional default when exhausted.

**Signature:** `anext(async_iterator, /)` or `anext(async_iterator, default, /)`

Added in Python 3.10; without a default, exhaustion raises `StopAsyncIteration`.

```python
value = await anext(iterator, None)
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#anext)

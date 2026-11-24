# ResourceWarning

Warning category for resource usage, such as an unclosed file. Ignored by default; use context managers to close resources reliably.

```python
with open('example.txt', encoding='utf-8') as f:
    text = f.read()
```

See [context managers](../../built_in_types/pages/context_managers.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#ResourceWarning)
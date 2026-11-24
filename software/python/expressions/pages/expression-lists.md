# Expression lists

A comma-separated expression list produces a tuple, except when used as part of a list or set display. A trailing comma makes a one-element tuple; parentheses are often useful but the comma is decisive. Starred expressions unpack iterables in supported contexts.

```python
one = 1,  # (1,)
combined = (0, *[1, 2])  # (0, 1, 2)
```

See [tuple](../../built_in_types/pages/tuple.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#expression-lists)
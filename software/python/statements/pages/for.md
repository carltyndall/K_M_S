# For statement

The iterable is evaluated once, then items are assigned to the target in order. The optional `else` runs on normal exhaustion, including an empty iterable, but not after `break`.

```python
for item in [1, 2]:
    print(item)
else:
    print('exhausted')
```

See [`for`](../../keywords/pages/for.md) and [iterables](../../built_in_types/pages/iterables.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
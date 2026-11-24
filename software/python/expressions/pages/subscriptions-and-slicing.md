# Subscriptions and slicing

`obj[key]` delegates subscription to the object; slices pass a `slice` object. For built-in sequences, slices use an exclusive stop and may specify a step. Custom objects can interpret keys differently.

```python
items = [0, 1, 2, 3]
items[1:4:2]  # [1, 3]
```

See [sequence operations](../../built_in_types/pages/sequence_operations.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#subscriptions)
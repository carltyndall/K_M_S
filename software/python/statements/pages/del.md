# Del statement

Deletion operates on targets: deleting a name unbinds it, whereas deleting a subscription or slice asks the container to remove it. Other references to the object are unaffected.

```python
items = [1, 2, 3]
del items[1:]  # [1]
```

See [`del`](../../keywords/pages/del.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-del-statement)
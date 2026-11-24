# Break statement

Break exits the nearest enclosing loop. Its loop `else` clause is skipped; intervening `finally` clauses still execute.

```python
for n in range(5):
    if n == 2:
        break
```

See [`break`](../../keywords/pages/break.md) and [for](for.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-break-statement)
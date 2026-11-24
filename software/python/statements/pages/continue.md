# Continue statement

Continue starts the next iteration of the nearest enclosing loop, after executing any intervening `finally` clauses.

```python
for n in range(3):
    if n == 1:
        continue
    print(n)  # 0, then 2
```

See [`continue`](../../keywords/pages/continue.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement)
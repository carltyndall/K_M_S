# While statement

The condition is re-evaluated before each iteration. An optional `else` suite runs when the condition becomes false, but not when the loop exits via `break`.

```python
n = 3
while n:
    n -= 1
else:
    print('finished')
```

See [`while`](../../keywords/pages/while.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
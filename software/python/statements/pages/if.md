# If statement

Conditions are tested in order; only the first matching suite executes. An optional `else` handles the remaining case.

```python
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'other'
```

See [`if`](../../keywords/pages/if.md), [`elif`](../../keywords/pages/elif.md) and [`else`](../../keywords/pages/else.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)
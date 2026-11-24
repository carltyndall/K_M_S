# Match statement

Pattern matching tries cases in order. A successful pattern can bind names; an optional guard must also be true before its suite runs. `_` is a wildcard in patterns, whereas a bare name captures a value.

```python
match (1, 2):
    case (x, y) if x < y:
        print(x, y)
    case _:
        pass
```

Available since Python 3.10. See [`match`](../../keywords/pages/match.md), [`case`](../../keywords/pages/case.md) and [`_`](../../keywords/pages/_.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
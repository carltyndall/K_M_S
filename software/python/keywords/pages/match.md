# match

`match` is a soft keyword introducing structural pattern matching; it remains an ordinary identifier outside that context. Added in Python 3.10.

```python
match (1, 2):
    case (x, y):
        print(x, y)  # 1 2
```

[Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
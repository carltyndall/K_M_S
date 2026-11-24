# assert

`assert` checks a condition and raises `AssertionError` if it is false. Assertions are omitted when optimization is enabled, so do not use them for essential validation.

```python
count = 3
assert count > 0, 'count must be positive'
```

[Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
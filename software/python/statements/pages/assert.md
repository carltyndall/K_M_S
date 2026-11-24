# Assert statement

Assertions are debugging checks, not input validation: optimized execution can omit both the condition and message evaluation.

```python
assert len([1, 2]) == 2, 'unexpected length'
```

See [`assert`](../../keywords/pages/assert.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
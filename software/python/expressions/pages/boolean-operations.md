# Boolean operations

`and` and `or` short-circuit and return an operand, not necessarily a Boolean; `not` returns a Boolean. Truth testing follows the object's truth-value rules.

```python
name = '' or 'guest'  # 'guest'
False and (1 / 0)  # False; right side is not evaluated
```

See [`and`](../../keywords/pages/and.md), [`or`](../../keywords/pages/or.md), [`not`](../../keywords/pages/not.md) and [Boolean operations](../../built_in_types/pages/boolean_operations.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#boolean-operations)
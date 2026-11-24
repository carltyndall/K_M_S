# Arithmetic conversions

When a built-in binary arithmetic operator has different numeric operand types, Python widens the narrower type: integer to floating point, then floating point to complex. User-defined types can implement their own operations.

```python
1 + 2.5  # 3.5
```

See [numeric types](../../built_in_types/pages/numeric_types.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#arithmetic-conversions)
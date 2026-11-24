# Arithmetic and matrix operations

Binary `+`, `-`, `*`, `/`, `//`, `%` and `@` perform addition, subtraction, multiplication, true division, floor division, remainder and matrix multiplication. `@` requires an operand type that implements it. Floor division rounds toward negative infinity; the remainder has the divisor's sign.

```python
(-7 // 3, -7 % 3, 7 / 3)  # (-3, 2, 2.333...)
```

See [numeric types](../../built_in_types/pages/numeric_types.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)
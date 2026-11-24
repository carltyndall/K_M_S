# Bitwise and shifting operations

`&`, `^` and `|` combine bits; `<<` shifts left and `>>` shifts right. For integers, right shift corresponds to floor division by a power of two; negative shift counts raise `ValueError`.

```python
(0b1100 & 0b1010, 3 << 2, -3 >> 1)  # (8, 12, -2)
```

See [integer bitwise operations](../../built_in_types/pages/integer_bitwise_operations.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#shifting-operations)
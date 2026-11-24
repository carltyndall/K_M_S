# Integer bitwise operations

Integer bitwise operations behave as though integers use two's complement with infinitely many sign bits. Shifts require a non-negative count; right shift corresponds to floor division by a power of two.

```python
5 & 3, 5 | 3, ~5, -5 >> 1  # (1, 7, -6, -3)
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#bitwise-operations-on-integer-types)
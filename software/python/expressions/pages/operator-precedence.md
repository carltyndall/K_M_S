# Operator precedence

Precedence determines grouping, not a general evaluation order. Power binds more tightly than unary operators on its left, but less tightly than unary operators on its right; exponentiation groups right to left. Comparisons chain, and Boolean `not`, `and`, `or` follow comparisons in decreasing precedence. Parentheses make intended grouping explicit.

```python
(-2**2, 2**-1, 2**3**2)  # (-4, 0.5, 512)
```

[Python documentation: complete precedence table](https://docs.python.org/3/reference/expressions.html#operator-precedence)
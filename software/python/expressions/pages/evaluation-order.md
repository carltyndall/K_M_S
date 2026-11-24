# Evaluation order

Expressions generally evaluate left to right. In an assignment, the right-hand side is evaluated before the targets. Short-circuiting operators and conditional expressions intentionally skip some operands.

```python
items = [0, 1]
i = 0
i, items[i] = 1, 9  # targets assigned left to right: items is [0, 9]
```

[Python documentation](https://docs.python.org/3/reference/expressions.html#evaluation-order)
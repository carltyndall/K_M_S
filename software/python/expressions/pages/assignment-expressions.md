# Assignment expressions

`:=` binds a name while producing the assigned value. Parentheses are required in several contexts, including an expression statement and many subexpressions.

```python
if (size := len('python')) > 5:
    print(size)  # 6
```

[Python documentation](https://docs.python.org/3/reference/expressions.html#assignment-expressions)
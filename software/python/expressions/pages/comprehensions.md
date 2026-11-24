# Comprehensions and generator expressions

Comprehensions build lists, sets or dictionaries from iteration and optional filters. Generator expressions produce values lazily. Their iteration variables do not leak into the enclosing scope; the leftmost iterable is evaluated in the enclosing scope.

```python
squares = [n * n for n in range(5) if n % 2 == 0]  # [0, 4, 16]
total = sum(n * n for n in range(3))  # 5
```

See [generators](../../built_in_types/pages/generators.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries)
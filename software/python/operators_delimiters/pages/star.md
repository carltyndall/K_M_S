# `*`

Multiplies values; also unpacks iterables in displays and calls, marks starred assignment targets, and separates keyword-only parameters in a function signature.

```python
2 * 3        # 6
[*range(3)]  # [0, 1, 2]
def f(*, x): return x
```

See [`**`](double_star.md), [`*=`](star_equal.md), and [expression lists](https://docs.python.org/3/reference/expressions.html#expression-lists).
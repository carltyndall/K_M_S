# Assignment

Assignment evaluates the right side before assigning targets left to right. Iterable unpacking supports one starred target per target list. Augmented assignment evaluates its target once and may modify an object in place; annotated assignment attaches an annotation to a target, with behavior depending on scope and Python version.

```python
first, *rest = [1, 2, 3]  # first = 1, rest = [2, 3]
rest += [4]
count: int = 3
```

See [assignment expressions](../../expressions/pages/assignment-expressions.md) and [annotations](annotations.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
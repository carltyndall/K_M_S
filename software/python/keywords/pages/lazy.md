# lazy

`lazy` is a soft keyword before an import statement, deferring the import until the imported name is used. It remains an ordinary identifier elsewhere. Added in Python 3.15; lazy imports are restricted to module scope and cannot be star imports or future statements.

```python
lazy import math
print(math.sqrt(9))  # Resolves the import when math is used.
```

[Python documentation](https://docs.python.org/3/reference/simple_stmts.html#lazy-imports)
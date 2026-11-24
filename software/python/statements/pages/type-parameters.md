# Type parameter lists

Python 3.12 introduced type parameter lists on generic functions, classes and type aliases. Parameters can include ordinary type variables, variadic type variables (`*Ts`) and parameter specifications (`**P`); bounds, constraints and defaults have additional version-specific rules.

```python
def identity[T](value: T) -> T:  # Python 3.12+
    return value
```

See [type aliases](type-aliases.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#type-parameter-lists)
# Type alias statement

Python 3.12 introduced the `type` statement for creating a `TypeAliasType`. Its value is evaluated lazily; optional type parameters support generic aliases.

```python
type Pair[T] = tuple[T, T]  # Python 3.12+
```

See [`type`](../../keywords/pages/type.md) and [type parameters](type-parameters.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-type-statement)
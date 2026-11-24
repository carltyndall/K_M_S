# Function definitions

Executing a definition creates a function and binds its name; its body runs on call. Default argument expressions are evaluated at definition time, so mutable defaults are shared. Decorators transform the function before binding it.

```python
def greet(name, *, prefix='Hello'):
    return f'{prefix}, {name}'
```

See [`def`](../../keywords/pages/def.md), [functions](../../built_in_types/pages/functions.md) and [annotations](annotations.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
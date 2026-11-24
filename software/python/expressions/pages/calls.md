# Calls

Calls evaluate a callable and arguments, then bind arguments to parameters. `*` expands positional arguments and `**` expands keyword mappings; duplicate or incompatible arguments raise `TypeError`.

```python
def greet(name, *, punctuation='!'):
    return name + punctuation

greet(*['Ada'], **{'punctuation': '.'})  # 'Ada.'
```

[Python documentation](https://docs.python.org/3/reference/expressions.html#calls)
# EOFError

Raised by [`input()`](../../built_in_functions/pages/input.md) when it encounters end-of-file without reading data.

```python
try:
    line = input('> ')
except EOFError:
    line = None
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#EOFError)
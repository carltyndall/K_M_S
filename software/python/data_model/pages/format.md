# `__format__`

`__format__(self, format_spec)` returns a string for `format()` and formatted string literals. Interpret the format specification according to the type; `object.__format__` only accepts an empty specification.

```python
class Number:
    def __format__(self, spec):
        return format(42, spec)

assert f'{Number():04d}' == '0042'
```

See [formatted string literals](../../built_in_types/pages/f_strings.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__format__).
# `__class_getitem__`

`__class_getitem__(cls, item)` can customize subscripting a class, commonly for generic types. A metaclass `__getitem__` takes precedence when present. Its use outside typing is discouraged by the documentation.

```python
class Example:
    def __class_getitem__(cls, item): return (cls, item)

assert Example[int] == (Example, int)
```

See [generic aliases](../../built_in_types/pages/generic_alias.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__).
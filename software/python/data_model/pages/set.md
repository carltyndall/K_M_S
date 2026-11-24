# `__set__`

`__set__(self, instance, value)` handles assignment to an attribute managed by a descriptor. Defining it makes the descriptor a data descriptor.

```python
class Field:
    def __set__(self, instance, value): instance.__dict__['value'] = value

class C:
    field = Field()

x = C()
x.field = 4
assert x.value == 4
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__set__) and the [grouped index](../01-grouped-index.md).

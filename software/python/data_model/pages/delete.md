# `__delete__`

`__delete__(self, instance)` handles deletion of an attribute managed by a descriptor. Defining it makes the descriptor a data descriptor.

```python
class Field:
    def __delete__(self, instance): del instance.__dict__['value']

class C:
    field = Field()

x = C()
x.value = 4
del x.field
assert 'value' not in x.__dict__
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#object.__delete__) and the [grouped index](../01-grouped-index.md).

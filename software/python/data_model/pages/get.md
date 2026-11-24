# Descriptor methods: `__get__`, `__set__`, `__delete__`

Descriptors customize attribute access when stored on a class. `__get__(self, instance, owner)` reads, `__set__(self, instance, value)` writes, and `__delete__(self, instance)` deletes. Class access passes `None` as the instance. Descriptors with a set or delete method are data descriptors and take precedence over instance attributes.

```python
class Constant:
    def __get__(self, instance, owner): return 42

class C:
    answer = Constant()

assert C().answer == 42
```

See [attribute access](attribute_access.md), [`__set_name__`](set_name.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#implementing-descriptors).
# Attribute access and descriptors

Ordinary instance lookup considers data descriptors, the instance dictionary, and non-data descriptors/class attributes. A descriptor implements one or more of `__get__`, `__set__` and `__delete__`; methods are non-data descriptors. Overriding `__getattribute__` can change this behavior, so delegate to the base implementation when appropriate.

```python
class C:
    @property
    def answer(self):
        return 42

assert C().answer == 42
```

See [descriptor methods](get.md), [`__getattr__`](getattr.md), [`__getattribute__`](getattribute.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#implementing-descriptors).
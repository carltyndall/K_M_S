# `__init_subclass__`

`__init_subclass__(cls, **kwargs)` customizes subclasses when they are created, without requiring a custom metaclass. Consume your own class keywords and forward the rest with `super()`; the default implementation rejects unexpected arguments.

```python
class Base:
    def __init_subclass__(cls, *, label, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.label = label

class Child(Base, label='child'): pass
assert Child.label == 'child'
```

See [class creation](classes.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__).
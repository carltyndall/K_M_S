# Classes and class creation

Classes are objects; their instances find behavior through their type and its method resolution order. Class creation resolves bases, selects a metaclass, prepares a namespace, executes the class body, then creates the class. Descriptors receive `__set_name__`, and the parent class's `__init_subclass__` runs.

```python
class Base:
    pass

class Child(Base):
    pass
assert Child.__mro__[:2] == (Child, Base)
```

See [`class`](../../keywords/pages/class.md), [classes and instances](../../built_in_types/pages/classes_and_instances.md), [`__init_subclass__`](init_subclass.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation).
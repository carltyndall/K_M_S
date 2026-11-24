# Class definitions

Executing a class definition runs its suite in a new namespace, then constructs and binds the class. Bases, metaclasses and decorators can customize construction.

```python
class Point:
    def __init__(self, x):
        self.x = x
```

See [`class`](../../keywords/pages/class.md) and [classes and instances](../../built_in_types/pages/classes_and_instances.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#class-definitions)
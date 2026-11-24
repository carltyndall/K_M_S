# `__subclasses__`

`cls.__subclasses__()` returns a list of the currently live immediate subclasses of a class, in definition order. It does not recursively include descendants; Python keeps weak references to the subclasses.

```python
class Base: pass
class Child(Base): pass

assert Child in Base.__subclasses__()
```

See [classes and class creation](classes.md) and the [Python data model](https://docs.python.org/3/reference/datamodel.html#type.__subclasses__).
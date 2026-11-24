# `__prepare__`

`__prepare__(metacls, name, bases, **kwargs)` supplies the namespace used to execute a class body. It is defined on the metaclass and is normally a class method.

```python
class Meta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs): return {}

class C(metaclass=Meta):
    answer = 42

assert C.answer == 42
```

See the [Python data model](https://docs.python.org/3/reference/datamodel.html#preparing-the-class-namespace) and the [grouped index](../01-grouped-index.md).

# Special method lookup

Implicit special operations usually look up methods on the type, bypassing the instance dictionary and generally even `__getattribute__`. Assigning a special method to one instance therefore does not reliably customize syntax or built-ins.

```python
class Box:
    def __len__(self):
        return 2

b = Box()
b.__len__ = lambda: 10
assert len(b) == 2
```

See [`__len__`](len.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#special-method-lookup).
# property

Create a managed attribute using getter, setter, and deleter methods.

**Signature:** `property(fget=None, fset=None, fdel=None, doc=None)`

```python
class C:
    @property
    def value(self):
        return 42
C().value  # 42
```

[Runnable property MWE](../../05-projects/property_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#property)

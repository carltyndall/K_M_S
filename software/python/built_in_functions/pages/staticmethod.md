# staticmethod

Wrap a method so it does not receive an implicit instance or class argument.

**Signature:** `staticmethod(function, /)`

```python
class C:
    @staticmethod
    def add(a, b):
        return a + b
C.add(1, 2)  # 3
```

[Runnable staticmethod MWE](../../05-projects/staticmethod_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#staticmethod)

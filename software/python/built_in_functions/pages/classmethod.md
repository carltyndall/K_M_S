# classmethod

Wrap a method so it receives the class as its first argument.

**Signature:** `classmethod(function, /)`

```python
class C:
    @classmethod
    def name(cls):
        return cls.__name__
C.name()  # 'C'
```

[Runnable classmethod MWE](../../05-projects/classmethod_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#classmethod)

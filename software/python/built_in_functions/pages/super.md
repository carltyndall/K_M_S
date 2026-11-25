# super

Return a proxy for delegating method calls to a parent or sibling class in the method resolution order.

**Signature:** `super(); super(type, object_or_type=None)`

```python
class A:
    def name(self): return 'A'
class B(A):
    def name(self): return super().name()
B().name()  # 'A'
```

[Runnable super MWE](../../05-projects/super_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#super)

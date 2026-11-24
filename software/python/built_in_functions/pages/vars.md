# vars

Return an object's `__dict__`, or the local namespace if no argument is supplied.

**Signature:** `vars()` or `vars(object, /)`

Objects without `__dict__` raise `TypeError`.

```python
class C: pass
x = C()
x.a = 1
vars(x)  # {'a': 1}
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#vars)

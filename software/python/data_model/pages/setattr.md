# `__setattr__` and `__delattr__`

`__setattr__(self, name, value)` handles attribute assignment; `__delattr__(self, name)` handles deletion. Delegate to `object` to perform the normal operation without recursively invoking the hook.

```python
class C:
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

c = C()
c.x = 1
assert c.x == 1
```

See [`del`](../../keywords/pages/del.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__setattr__).
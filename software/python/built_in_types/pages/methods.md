# Methods

A bound instance method combines a function with an instance. Calling it passes the instance as the function's first argument; `__self__` identifies that instance.

```python
class Example:
    def value(self):
        return 42
obj = Example()
obj.value.__self__ is obj  # True
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#methods)
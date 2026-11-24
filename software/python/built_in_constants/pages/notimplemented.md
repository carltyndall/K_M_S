# NotImplemented

Binary and in-place special methods can return `NotImplemented` to signal that an operation is unsupported for the other operand's type. Python then tries the reflected operation or another appropriate fallback. It is not the same as the `NotImplementedError` exception.

```python
class Example:
    def __eq__(self, other):
        if not isinstance(other, Example):
            return NotImplemented
        return True
```

Do not use it as a Boolean: this raises `TypeError` in Python 3.14 and later; it was deprecated from 3.9.

[Python documentation](https://docs.python.org/3/builtins/constants.html#NotImplemented)
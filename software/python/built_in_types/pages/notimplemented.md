# NotImplemented

`NotImplemented` is a singleton that binary special methods can return to indicate that an operation is unsupported for the operands. It is not the same as raising `NotImplementedError` and must not be used as a Boolean.

```python
int.__add__(1, 'x') is NotImplemented  # True
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#the-notimplemented-object)
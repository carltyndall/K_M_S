# Truth value testing

Objects are true by default unless `__bool__()` returns `False` or `__len__()` returns zero. Empty containers, numeric zero and `None` are false.

```python
bool([]), bool([0])  # (False, True)
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#truth-value-testing)
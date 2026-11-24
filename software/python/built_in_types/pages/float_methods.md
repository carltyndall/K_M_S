# Float methods

Floats expose their exact stored value through methods such as `as_integer_ratio()` and `hex()`. `is_integer()` tests whether a finite float has an integral value.

```python
(0.5).as_integer_ratio()  # (1, 2)
(2.0).is_integer()  # True
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#additional-methods-on-float)
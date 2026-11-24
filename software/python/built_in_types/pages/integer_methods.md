# Integer methods

Integers provide methods such as `bit_length()`, `bit_count()`, `to_bytes()` and `from_bytes()` for inspecting and converting their binary representation.

```python
(13).bit_count()  # 3
int.from_bytes(b'\x01\x00', 'big')  # 256
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#additional-methods-on-integer-types)
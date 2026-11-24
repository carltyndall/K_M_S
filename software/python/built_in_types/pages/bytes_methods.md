# Bytes and bytearray operations

Bytes and bytearray offer searching, splitting, replacing and other methods analogous to string methods. Many character-oriented operations are defined in terms of ASCII, not arbitrary text encodings.

```python
b'a,b'.replace(b',', b':')  # b'a:b'
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#bytes-and-bytearray-operations)
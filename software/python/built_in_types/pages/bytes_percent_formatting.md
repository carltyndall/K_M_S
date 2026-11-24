# printf-style bytes formatting

Bytes and bytearrays support `%` formatting with bytes-oriented conversion specifiers. The result has the same binary sequence type as the format operand.

```python
b'%s: %d' % (b'count', 3)  # b'count: 3'
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#printf-style-bytes-formatting)
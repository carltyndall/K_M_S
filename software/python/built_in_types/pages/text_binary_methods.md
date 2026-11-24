# Text and binary sequence methods

Strings, bytes and bytearrays share a number of operations, such as splitting, searching and replacing, but their element types and accepted arguments differ. Binary methods generally work with bytes-like objects and some assume ASCII-compatible data.

```python
'a,b'.split(',')  # ['a', 'b']
b'a,b'.split(b',')  # [b'a', b'b']
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#text-and-binary-sequence-type-methods-summary)
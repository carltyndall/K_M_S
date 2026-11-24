# BytesWarning

Warning category for potentially problematic operations involving bytes or bytearray. The `-b` option enables these warnings; `-bb` turns them into errors.

```python
# Run with python -b:
print(b'hello' == 'hello')  # False, with BytesWarning
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#BytesWarning)
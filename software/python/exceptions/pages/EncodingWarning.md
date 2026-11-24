# EncodingWarning

Warning category for use of a default text encoding. Added in Python 3.10; opt in with `-X warn_default_encoding` or `PYTHONWARNDEFAULTENCODING`.

```python
# With the opt-in enabled, this may warn about the default encoding:
with open('example.txt') as f:
    text = f.read()
```

See [`open`](../../built_in_functions/pages/open.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#EncodingWarning)
# open

Open a file and return a file object; use a context manager to close it reliably.

**Signature:** `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`

Text encoding defaults are platform-dependent; specify one when appropriate.

```python
with open('example.txt', encoding='utf-8') as f:
    text = f.read()
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#open)

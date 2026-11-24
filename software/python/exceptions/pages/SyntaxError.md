# SyntaxError

Raised when Python cannot parse source. Attributes include `filename`, `lineno`, `offset`, `text`, `end_lineno`, and `end_offset` when available.

```python
try:
    compile('if:', '<input>', 'exec')
except SyntaxError as exc:
    print(exc.lineno, exc.msg)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#SyntaxError)
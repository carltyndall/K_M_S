# IndentationError

A [`SyntaxError`](SyntaxError.md) caused by incorrect indentation.

```python
compile('if True:\npass\n', '<input>', 'exec')  # IndentationError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#IndentationError)
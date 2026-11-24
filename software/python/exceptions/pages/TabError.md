# TabError

An [`IndentationError`](IndentationError.md) caused by inconsistent use of tabs and spaces in indentation.

```python
compile('if True:\n\tpass\n        pass\n', '<input>', 'exec')  # TabError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#TabError)
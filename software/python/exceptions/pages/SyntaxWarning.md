# SyntaxWarning

Warning category for dubious syntax. Often emitted while compiling source, so runtime warning filters may not affect it.

```python
import warnings
warnings.warn('dubious syntax', SyntaxWarning)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#SyntaxWarning)
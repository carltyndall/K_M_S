# PythonFinalizationError

A [`RuntimeError`](RuntimeError.md) raised when an operation is blocked during interpreter shutdown. Added in Python 3.13; affected operations vary by version.

```python
import sys
if sys.is_finalizing():
    print('Avoid starting new work during shutdown')
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#PythonFinalizationError)
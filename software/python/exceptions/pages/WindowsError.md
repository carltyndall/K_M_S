# WindowsError

Windows-only legacy alias of [`OSError`](OSError.md). Do not rely on this name in portable code.

```python
import sys
if sys.platform == 'win32':
    assert WindowsError is OSError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#WindowsError)
# SystemExit

A direct [`BaseException`](BaseException.md) subclass raised by `sys.exit()`. Its `code` attribute carries the exit status or message; `finally` blocks still execute.

```python
import sys
sys.exit(2)  # raises SystemExit(2)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#SystemExit)
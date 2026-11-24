# FileExistsError

An [`OSError`](OSError.md) raised when creating an already existing file or directory, corresponding to `EEXIST`.

```python
from pathlib import Path
Path('.').mkdir()  # FileExistsError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#FileExistsError)
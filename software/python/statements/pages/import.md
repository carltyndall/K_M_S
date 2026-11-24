# Import statement

Import finds and initializes modules as needed, then binds names in the current scope. `from` imports selected attributes; relative imports use leading dots within packages.

```python
import math as m
from math import sqrt
sqrt(9) == m.sqrt(9)  # True
```

See [`import`](../../keywords/pages/import.md), [`from`](../../keywords/pages/from.md), and [`lazy`](../../keywords/pages/lazy.md) for version-specific lazy imports. [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
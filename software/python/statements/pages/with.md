# With statement

A context manager's enter method supplies the optional target; its exit method runs when the suite leaves, including on exceptions. Multiple managers are entered left to right and exited in reverse order.

```python
from contextlib import nullcontext
with nullcontext(42) as value:
    print(value)
```

See [`with`](../../keywords/pages/with.md) and [context managers](../../built_in_types/pages/context_managers.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
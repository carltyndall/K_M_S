# exec

Execute Python statements from a string or code object in the supplied namespaces.

**Signature:** `exec(source, globals=None, locals=None, *, closure=None)`

Never execute untrusted input. The `closure` parameter was added in Python 3.11; `globals` and `locals` can be passed by keyword starting in Python 3.13.

```python
namespace = {}
exec('x = 5', namespace)
namespace['x']  # 5
```

[Runnable exec MWE](../../05-projects/exec_mwe.py) — run instructions are in the [Python projects guide](../../05-projects/README.md).

[Python documentation](https://docs.python.org/3/builtins/functions.html#exec)

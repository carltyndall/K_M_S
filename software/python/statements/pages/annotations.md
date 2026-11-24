# Annotations

Annotations attach expressions to function parameters, return values and annotated assignments. They are not enforced as runtime type checks. Evaluation and storage rules depend on scope, Python version and `from __future__ import annotations`; consult the reference before relying on evaluation timing.

```python
def repeat(text: str, times: int) -> str:
    return text * times
```

See [assignment](assignment.md). [Python documentation](https://docs.python.org/3/reference/compound_stmts.html#annotations)
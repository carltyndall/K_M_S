# eval

Evaluate a Python expression in the supplied namespaces.

**Signature:** `eval(source, globals=None, locals=None)`

Never evaluate untrusted input: it can execute arbitrary code.

```python
eval('2 + 3')  # 5
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#eval)

# compile

Compile source into a code object for evaluation or execution.

**Signature:** `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)`

```python
code = compile('2 + 3', '<example>', 'eval')
eval(code)  # 5
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#compile)

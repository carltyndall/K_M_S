# __import__

Low-level import function used by the import statement; normally prefer `import` or `importlib.import_module`.

**Signature:** `__import__(name, globals=None, locals=None, fromlist=(), level=0)`

```python
math = __import__('math')
math.sqrt(9)  # 3.0
```

[Python documentation](https://docs.python.org/3/builtins/functions.html#import__)

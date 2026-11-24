# Internal objects

Python exposes several interpreter-internal object types, including code, frame and traceback objects. Their details are primarily useful for introspection, debugging and implementation tooling.

```python
try:
    1 / 0
except ZeroDivisionError as exc:
    traceback = exc.__traceback__
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#internal-objects)
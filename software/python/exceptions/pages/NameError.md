# NameError

Raised when a local or global name cannot be found. The `name` attribute identifies the missing name.

```python
try:
    missing_name
except NameError as exc:
    print(exc.name)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#NameError)
# AttributeError

Raised when an attribute reference or assignment fails. `name` and `obj` can identify the missing attribute and its object.

```python
try:
    (1).missing
except AttributeError as exc:
    print(exc.name)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#AttributeError)
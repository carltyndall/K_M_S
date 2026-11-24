# Generic alias type

Parameterizing a standard generic class creates a `types.GenericAlias`, which preserves its origin and type arguments for introspection. Instances created from it do not enforce those arguments at runtime.

```python
list[int].__origin__  # <class 'list'>
list[int].__args__  # (<class 'int'>,)
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#generic-alias-type)
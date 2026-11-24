# ModuleNotFoundError

An [`ImportError`](ImportError.md) raised when a module cannot be located, or when `None` is found in `sys.modules` for it. Inspect `name` before assuming the missing module is the one you requested: a dependency may be missing instead.

```python
try:
    import a_module_that_does_not_exist
except ModuleNotFoundError as exc:
    print(exc.name)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError)
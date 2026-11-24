# __debug__

`__debug__` is `True` unless Python was started with the `-O` option. Assignment to it is a syntax error. Assertions are omitted under optimization.

```python
if __debug__:
    print('debugging enabled')
```

[Python documentation](https://docs.python.org/3/builtins/constants.html#debug__)
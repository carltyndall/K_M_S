# BaseExceptionGroup

Groups multiple exceptions, including direct [`BaseException`](BaseException.md) subclasses. `message` and `exceptions` expose its contents; `subgroup()` and `split()` preserve matching nested structure. Added in Python 3.11.

```python
group = BaseExceptionGroup('shutdown', [KeyboardInterrupt(), ValueError('bad')])
print(group.subgroup(ValueError))
```

See [`ExceptionGroup`](ExceptionGroup.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup)
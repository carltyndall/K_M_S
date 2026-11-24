# DeprecationWarning

Warning category for deprecated features aimed at other Python developers. Normally ignored by default outside `__main__`; enable it during testing.

```python
import warnings
warnings.warn('old API is deprecated', DeprecationWarning)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#DeprecationWarning)
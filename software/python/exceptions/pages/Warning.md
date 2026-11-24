# Warning

Base class for warning categories. Warnings are usually emitted through `warnings.warn()` and controlled by warning filters; filters can turn them into exceptions.

```python
import warnings
warnings.warn('check configuration', UserWarning)
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#Warning)
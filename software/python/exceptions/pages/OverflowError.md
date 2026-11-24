# OverflowError

An [`ArithmeticError`](ArithmeticError.md) raised when a numerical result is too large to represent. Python integers themselves have arbitrary precision, subject to available memory.

```python
import math
math.exp(1000)  # OverflowError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#OverflowError)
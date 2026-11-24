# Integer string conversion length limitation

Python limits potentially expensive conversions between integers and non-power-of-two-base strings to mitigate denial-of-service attacks. The limit is configurable; power-of-two bases and byte conversions are not subject to this limit.

```python
import sys
sys.get_int_max_str_digits()  # current limit; 0 means disabled
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#integer-string-conversion-length-limitation)
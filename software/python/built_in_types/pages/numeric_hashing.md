# Hashing of numeric types

Numeric hashes are designed so equal numeric values have equal hashes, even across numeric types. Hashes of rational values are based on reduction modulo a fixed prime.

```python
hash(1) == hash(1.0)  # True
```

[Python documentation](https://docs.python.org/3.15/library/stdtypes.html#hashing-of-numeric-types)
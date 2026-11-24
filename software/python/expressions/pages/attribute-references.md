# Attribute references

`object.name` asks the object for an attribute; lookup can invoke descriptors or custom attribute access. The resulting value may be a bound method.

```python
text = 'hello'
text.upper()  # 'HELLO'
```

[Python documentation](https://docs.python.org/3/reference/expressions.html#attribute-references)
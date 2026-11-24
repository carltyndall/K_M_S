# Identity, type and value

Every object has an identity, a type and a value. Identity is stable during an object's lifetime; `is` compares identity, whereas `==` compares values using rich comparison. Mutability depends on type; an immutable container can still refer to mutable objects.

```python
a = [1]
b = [1]
assert a == b and a is not b
```

See [`is`](../../keywords/pages/is.md), [comparisons](../../built_in_types/pages/comparisons.md), [`__eq__`](eq.md), and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types).
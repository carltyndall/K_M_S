# Lambdas

A lambda creates an anonymous function whose body is a single expression. Parameters support many of the same forms as function definitions, but annotations are not allowed in lambda syntax.

```python
sorted(['bbb', 'a'], key=lambda text: len(text))  # ['a', 'bbb']
```

See [`lambda`](../../keywords/pages/lambda.md) and [function definitions](../../statements/pages/function-definitions.md). [Python documentation](https://docs.python.org/3/reference/expressions.html#lambdas)
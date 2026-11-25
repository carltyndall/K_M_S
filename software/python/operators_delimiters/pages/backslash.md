# `\`

Introduces escape sequences in string literals and joins physical lines when it ends a line outside a string or comment. It is not a standalone operator.

```python
text = 'a\nb'
x = 1 + \
    2
```

See [explicit line joining](https://docs.python.org/3/reference/lexical_analysis.html#explicit-line-joining) and [escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences).
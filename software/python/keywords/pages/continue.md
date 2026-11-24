# continue

`continue` skips the rest of the current iteration of the nearest enclosing loop and continues with the next iteration.

```python
for number in range(3):
    if number == 1:
        continue
    print(number)  # 0, then 2
```

[Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement)
# Pure Python: Exercises

## Exercise 1: A study-session record

**Module:** 1 — Think in Python  
**Practice:** Names, values, types, expressions, and the REPL

Open the Python REPL (on Windows, try `py` in PowerShell) and enter the following one line at a time. Before each line, predict what kind of value it will produce.

```python
topic = "Python basics"
first_block_minutes = 20
second_block_minutes = 15
finished = True

type(topic)
type(first_block_minutes)
type(finished)

total_minutes = first_block_minutes + second_block_minutes
total_minutes
total_minutes / 5
print("Topic:", topic, "| total minutes:", total_minutes, "| finished:", finished)
```

### Check your understanding

1. Which lines assign values to names, and which lines are expressions you inspect?
2. What are the types of `topic`, `first_block_minutes`, and `finished`?
3. What value does `total_minutes / 5` produce, and why is it a different type from `total_minutes`?
4. Change `second_block_minutes` to `25`, then rerun the assignment that calculates `total_minutes`. What changed, and what did not?

### Solution notes

* `topic`, `first_block_minutes`, `second_block_minutes`, and `finished` are names bound to a string, two integers, and a Boolean value respectively.
* `type(...)` is an expression that evaluates to type information; `total_minutes` evaluates to the integer `35` after the initial assignments.
* `total_minutes / 5` evaluates to `7.0` (`float`), because `/` performs true division in Python, even when the result is a whole number.
* After changing `second_block_minutes` to `25`, re-run `total_minutes = first_block_minutes + second_block_minutes`, then inspect `total_minutes` again: the new result is `45`. Names keep their assigned values until code assigns them a new value.
* The final `print(...)` call displays a readable summary using the current values. Your output should show the topic, `35` total minutes, and `True` before you make the change.

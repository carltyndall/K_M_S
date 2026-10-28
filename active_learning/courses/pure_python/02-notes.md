# Pure Python: Notes

## Module 1 — Think in Python

### What programming is

A program is a set of instructions that transforms information into a result. Learning to program means learning to describe a problem as precise steps, then checking whether the computer's result matches the intended result. Python syntax is the notation for those instructions, not the whole programming skill.

### The REPL and scripts

The Python REPL (read-evaluate-print loop) accepts an expression, evaluates it, and displays the result. It is useful for trying one idea at a time. A script is saved code that can be run again; use the REPL for quick experiments and scripts when a sequence should be kept and repeated.

On Windows, start an installed interpreter from PowerShell with `py`. If that launcher is unavailable, use the Python command or editor configured on the machine.

### Values, types, names, and expressions

* A **value** is information the program can work with, such as `7`, `2.5`, `"hello"`, or `True`.
* A **type** describes the kind of value. Common starting types are `int`, `float`, `str`, and `bool`; inspect a value with `type(value)`.
* A **name** lets code refer to a value. Assignment, such as `minutes = 25`, binds a name to the value on the right. `=` means assignment here, not a claim that two things are equal.
* An **expression** is code that evaluates to a value. For example, `minutes * 2` evaluates to `50` when `minutes` is `25`.

Try these one line at a time in the REPL:

```python
minutes = 25
type(minutes)
minutes * 2
topic = "Python basics"
type(topic)
```

The REPL displays the result of each expression. Assignment changes or creates a name, so it does not display the assigned value automatically; enter the name on its own line to inspect it.

### A useful learning loop

Predict what an expression will do, run it, inspect the result, and explain any mismatch. Change one part at a time so the cause of a changed result stays clear. Keep reusable language mental models in [`concepts/`](../../../concepts/README.md); the course records the learning sequence and practice.

For a separate reference on interpreter execution and the language's broader building blocks, see [`Python: Core Concepts`](../../../software/python/02-core-concepts.md). This module stays focused on the REPL, values, names, types, and expressions rather than repeating that reference.

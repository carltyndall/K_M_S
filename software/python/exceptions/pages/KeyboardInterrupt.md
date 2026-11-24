# KeyboardInterrupt

A direct [`BaseException`](BaseException.md) subclass raised when the user interrupts execution, usually with Ctrl-C. It can arrive at unpredictable points; generally let it terminate the program.

```python
try:
    input('Press Ctrl-C: ')
except KeyboardInterrupt:
    print('Interrupted')
    raise
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt)
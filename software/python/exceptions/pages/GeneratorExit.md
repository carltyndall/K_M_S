# GeneratorExit

A direct [`BaseException`](BaseException.md) subclass injected into a generator or coroutine when it is closed. Cleanup belongs in `finally`; do not yield another value when handling closure.

```python
def stream():
    try:
        yield 1
    finally:
        print('closed')

g = stream()
next(g)
g.close()
```

See [generators](../../built_in_types/pages/generators.md). [Python documentation](https://docs.python.org/3/library/exceptions.html#GeneratorExit)
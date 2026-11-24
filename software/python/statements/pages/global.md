# Global statement

The declaration directs name binding in the current code block to the module namespace. It is a parser directive and must precede uses or assignments of those names in the block.

```python
count = 0
def increment():
    global count
    count += 1
```

See [`global`](../../keywords/pages/global.md). [Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)
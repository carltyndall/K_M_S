# exit

`exit` is added by `site` for interactive use. Calling it raises `SystemExit` with an optional exit code; displaying it gives exit instructions. Prefer `sys.exit()` in programs.

```python
exit(0)  # raises SystemExit with code 0
```

[Python documentation](https://docs.python.org/3/builtins/constants.html#exit)
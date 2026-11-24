# path entry hook

A callable in `sys.path_hooks` that accepts a path entry and returns a finder for it, or raises `ImportError` if it cannot handle the entry.

[Python glossary](https://docs.python.org/3/glossary.html#term-path-entry-hook)
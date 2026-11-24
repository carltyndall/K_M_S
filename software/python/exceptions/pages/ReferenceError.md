# ReferenceError

Raised when a weak-reference proxy accesses an object that has already been garbage collected.

```python
import weakref
class Item: pass
item = Item()
proxy = weakref.proxy(item)
del item
print(proxy)  # ReferenceError
```

[Python documentation](https://docs.python.org/3/library/exceptions.html#ReferenceError)
# `__set_name__`

During class creation, `type.__new__` calls `__set_name__(self, owner, name)` on class attributes that define it. Attributes assigned after creation need an explicit call if notification is required.

```python
class Field:
    def __set_name__(self, owner, name): self.name = name

class Record:
    title = Field()

assert Record.title.name == 'title'
```

See [descriptors](get.md) and the [Python documentation](https://docs.python.org/3/reference/datamodel.html#object.__set_name__).
# itertools

`itertools` composes efficient, usually lazy [iterators](../../built_in_types/pages/iterators.md). Consume them with a [`for`](../../keywords/pages/for.md) loop or convert a finite result to a [`list`](../../built_in_types/pages/list.md).

```python
from itertools import chain, combinations, groupby, islice, count

print(list(chain([1, 2], [3])))  # [1, 2, 3]
print(list(islice(count(10), 3)))  # [10, 11, 12]
print(list(combinations('ABC', 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
items = ['a', 'a', 'b']
print([(key, list(group)) for key, group in groupby(items)])  # [('a', ['a', 'a']), ('b', ['b'])]
```

`count()` is infinite, so bound consumption (for example with `islice`). `groupby()` groups consecutive equal keys, not all equal keys globally; sort first if appropriate. Group iterators share the underlying input, so consume each group before advancing.

[Python documentation](https://docs.python.org/3/library/itertools.html)
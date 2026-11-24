# collections

`collections` provides specialized containers beyond the built-in [`dict`](../../built_in_types/pages/dict.md), [`list`](../../built_in_types/pages/list.md), and [`tuple`](../../built_in_types/pages/tuple.md).

```python
from collections import Counter, defaultdict, deque

counts = Counter('banana')
print(counts.most_common(1))  # [('a', 3)]
groups = defaultdict(list)
for key, value in [('a', 1), ('b', 2), ('a', 3)]:
    groups[key].append(value)
print(dict(groups))  # {'a': [1, 3], 'b': [2]}
queue = deque([1, 2])
queue.append(3)
print(queue.popleft())  # 1
```

`Counter` counts hashable items; `defaultdict` calls its factory when a missing key is accessed with `[]`. A `deque` supports efficient appends and pops at either end. `namedtuple` creates tuple subclasses with named fields. See also [`for`](../../keywords/pages/for.md).

[Python documentation](https://docs.python.org/3/library/collections.html)
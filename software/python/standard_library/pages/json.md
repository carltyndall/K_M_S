# json

`json` converts between JSON text and Python values. Use `dumps`/`loads` for strings and `dump`/`load` for text files.

```python
import json

record = {'name': 'Ada', 'scores': [3, 5], 'active': True}
text = json.dumps(record, indent=2)
print(json.loads(text) == record)  # True
with open('record.json', 'w', encoding='utf-8') as file:
    json.dump(record, file, indent=2)
with open('record.json', encoding='utf-8') as file:
    restored = json.load(file)
```

JSON objects become [`dict`](../../built_in_types/pages/dict.md) values and arrays become [`list`](../../built_in_types/pages/list.md) values; JSON object keys are strings. Not every Python object is directly serializable, and tuples become arrays, so round trips need not preserve types. Invalid JSON raises `json.JSONDecodeError`; see [`try` and `except`](../../keywords/pages/try.md). For strict JSON output, pass `allow_nan=False` to reject non-finite floats.

[Python documentation](https://docs.python.org/3/library/json.html)
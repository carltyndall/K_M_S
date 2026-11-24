# re

`re` searches, matches, splits, and substitutes text using regular expressions. Raw string literals keep Python from interpreting backslashes in patterns.

```python
import re

text = 'Order AB-42, order CD-17'
pattern = re.compile(r'([A-Z]{2})-(\d+)')
match = pattern.search(text)
if match:
    print(match.group(1), match.group(2))  # AB 42
print(pattern.findall(text))  # [('AB', '42'), ('CD', '17')]
print(pattern.sub('REDACTED', text))  # Order REDACTED, order REDACTED
```

`search` finds a match anywhere, `match` starts at the beginning, and `fullmatch` requires the entire string to match. A failed search returns `None`; check it before accessing groups. Use `re.escape()` for literal user-provided text in a pattern, and take care with untrusted patterns that may be slow. See [`str`](../../built_in_types/pages/str.md) and [`if`](../../keywords/pages/if.md).

[Python documentation](https://docs.python.org/3/library/re.html)
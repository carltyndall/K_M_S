# pathlib

`pathlib` represents filesystem paths as objects. Joining paths with `/` constructs a path; it does not create a file or directory.

```python
from pathlib import Path

folder = Path('notes')
folder.mkdir(parents=True, exist_ok=True)
file = folder / 'ideas.txt'
file.write_text('Hello\n', encoding='utf-8')
print(file.read_text(encoding='utf-8'))
print(file.name, file.suffix)  # ideas.txt .txt
print(sorted(folder.glob('*.txt')))  # matching paths
```

Relative paths are resolved against the current working directory, not the script's location. Filesystem operations can raise `OSError`; `exists()` is not a substitute for handling errors when opening a file. For streaming or large files use `file.open()` with [`with`](../../keywords/pages/with.md); see also [`str`](../../built_in_types/pages/str.md).

[Python documentation](https://docs.python.org/3/library/pathlib.html)
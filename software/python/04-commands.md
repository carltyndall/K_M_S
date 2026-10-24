# Python: Command Reference & Built-ins

Quick-lookup reference for Python CLI options and frequently used built-in functions.

## 💻 Command Line Flags
| Flag | Description | Example |
| :--- | :--- | :--- |
| `python -c "<code>"` | Execute single inline Python statement | `python -c "print(2 + 2)"` |
| `python -m <module>` | Run library module as a script | `python -m json.tool data.json` |
| `python -i <script.py>` | Run script and enter interactive REPL | `python -i test.py` |

## 🛠️ Essential Built-in Functions
- `print(*values)` — Outputs text to stdout.
- `len(sequence)` — Returns number of items.
- `type(object)` — Returns object data type.
- `range(start, stop, step)` — Generates a sequence of integers.
- `enumerate(iterable)` — Returns index and value pairs.

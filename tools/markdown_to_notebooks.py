#!/usr/bin/env -S uv run
"""Convert Python reference Markdown without overwriting existing notebooks.

Run with --check to verify notebook cells against their Markdown sources.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = (
    "built_in_constants", "built_in_functions", "built_in_types", "data_model",
    "exceptions", "expressions", "glossary", "keywords", "methods",
    "standard_library", "statements",
)


def notebook_path(markdown):
    name = markdown.stem
    name = name if name == "README" else name.lower().replace("-", "_")
    return markdown.with_name(f"{name}.ipynb")


def cells(text):
    result = []
    prose = []
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        if re.fullmatch(r"```python\s*", lines[i]):
            if prose:
                result.append(("markdown", "".join(prose)))
            prose = []
            i += 1
            code = []
            while i < len(lines) and not re.fullmatch(r"```\s*", lines[i]):
                code.append(lines[i])
                i += 1
            if i == len(lines):
                raise ValueError("Unclosed Python code fence")
            result.append(("code", "".join(code)))
        else:
            prose.append(lines[i])
        i += 1
    if prose:
        result.append(("markdown", "".join(prose)))
    return result


def notebook(text):
    notebook_cells = []
    for index, (cell_type, source) in enumerate(cells(text)):
        cell_id = hashlib.sha256(f"{index}:{cell_type}:{source}".encode()).hexdigest()[:16]
        cell = {"cell_type": cell_type, "id": cell_id, "metadata": {},
                "source": source.splitlines(keepends=True)}
        if cell_type == "code":
            cell.update(execution_count=None, outputs=[])
        notebook_cells.append(cell)
    return {"cells": notebook_cells, "metadata": {"kernelspec": {
        "display_name": "Python 3", "language": "python", "name": "python3"
    }, "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}


def check(markdown, path):
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual.get("nbformat") != 4 or not isinstance(actual.get("cells"), list):
        raise ValueError("Invalid notebook format")
    expected = [(kind, source.strip()) for kind, source in cells(markdown.read_text(encoding="utf-8"))]
    found = []
    for cell in actual["cells"]:
        source = cell["source"]
        if isinstance(source, list) and all(isinstance(s, str) for s in source):
            source = "".join(source)
        if not isinstance(source, str):
            raise ValueError("Invalid cell source")
        found.append((cell["cell_type"], source.strip()))
    if expected != found:
        raise ValueError("Notebook cells differ from Markdown")


def run(args):
    if args not in ([], ["--check"]):
        raise ValueError("Usage: uv run tools/markdown_to_notebooks.py [--check]")
    files = [path for section in SECTIONS
             for path in sorted((ROOT / "software" / "python" / section).rglob("*.md"))]
    destinations = {}
    for file in files:
        destinations.setdefault(notebook_path(file), []).append(file)
    collisions = {path: sources for path, sources in destinations.items() if len(sources) > 1}
    if collisions:
        raise ValueError(f"Notebook name collisions: {collisions}")
    created = 0
    errors = []
    for file in files:
        path = notebook_path(file)
        try:
            if not path.exists() and args != ["--check"]:
                path.write_text(json.dumps(notebook(file.read_text(encoding="utf-8")), indent=2,
                                           ensure_ascii=False) + "\n", encoding="utf-8")
                created += 1
            check(file, path)
        except (OSError, ValueError, KeyError, TypeError) as error:
            errors.append(f"{file.relative_to(ROOT)}: {error}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
    print(f"{len(files)} pairs checked; {created} created; {len(errors)} errors")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))

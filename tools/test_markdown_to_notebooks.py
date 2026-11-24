#!/usr/bin/env -S uv run
import json
import tempfile
import unittest
from pathlib import Path

import markdown_to_notebooks as converter


class MarkdownToNotebooksTest(unittest.TestCase):
    def test_cells_preserve_prose_and_python_examples(self):
        text = "# Example\n\n```python\nprint(1)\n```\n\n```text\nhello\n```\n"
        self.assertEqual([("markdown", "# Example\n\n"), ("code", "print(1)\n"),
                          ("markdown", "\n```text\nhello\n```\n")], converter.cells(text))
        notebook = converter.notebook(text)
        self.assertEqual(4, notebook["nbformat"])
        self.assertEqual([], notebook["cells"][1]["outputs"])
        self.assertIsNone(notebook["cells"][1]["execution_count"])

    def test_unclosed_fence_is_rejected(self):
        with self.assertRaises(ValueError):
            converter.cells("```python\nprint(1)\n")

    def test_names_follow_conventions(self):
        self.assertEqual(Path("01_grouped_index.ipynb"), converter.notebook_path(Path("01-grouped-index.md")))
        self.assertEqual(Path("syntaxerror.ipynb"), converter.notebook_path(Path("SyntaxError.md")))
        self.assertEqual(Path("README.ipynb"), converter.notebook_path(Path("README.md")))

    def test_check_detects_changed_content(self):
        with tempfile.TemporaryDirectory(prefix="notebook_test_", dir=converter.ROOT) as directory:
            markdown = Path(directory) / "example.md"
            path = Path(directory) / "example.ipynb"
            markdown.write_text("# Example\n", encoding="utf-8")
            path.write_text(json.dumps(converter.notebook(markdown.read_text(encoding="utf-8"))), encoding="utf-8")
            converter.check(markdown, path)
            markdown.write_text("# Changed\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                converter.check(markdown, path)


if __name__ == "__main__":
    unittest.main()

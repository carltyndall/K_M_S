#!/usr/bin/env -S uv run
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

import config
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

    def test_run_uses_configured_directories_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory(prefix="notebook_test_", dir=converter.ROOT) as directory:
            root = Path(directory)
            (root / "selected").mkdir()
            (root / "ignored").mkdir()
            markdown = root / "selected" / "example.md"
            markdown.write_text("# Example\n", encoding="utf-8")
            (root / "ignored" / "other.md").write_text("# Other\n", encoding="utf-8")
            settings = {"markdown_to_notebooks": {"directories": ["selected", "selected"]}}
            with patch.object(converter, "ROOT", root), patch.object(converter, "load_config", return_value=settings):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(0, converter.run([]))
                    self.assertFalse((root / "ignored" / "other.ipynb").exists())
                    path = markdown.with_suffix(".ipynb")
                    original = path.read_text(encoding="utf-8")
                    self.assertEqual(0, converter.run(["--check"]))
                    markdown.write_text("# Changed\n", encoding="utf-8")
                    with redirect_stderr(io.StringIO()):
                        self.assertEqual(1, converter.run([]))
                    self.assertEqual(original, path.read_text(encoding="utf-8"))

    def test_invalid_configuration_fails(self):
        for directories in ("wrong", ["../outside"], ["missing"]):
            settings = {"markdown_to_notebooks": {"directories": directories}}
            with self.subTest(directories=directories), patch.object(converter, "load_config", return_value=settings):
                with redirect_stderr(io.StringIO()):
                    self.assertEqual(1, converter.run(["--check"]))

    def test_launcher_settings_validate_config(self):
        settings = {"pycharm": {"default_path": "software/python", "cli_launchers": ["my launcher"],
                                "macos_apps": ["My PyCharm"]}}
        self.assertEqual(("software/python", ["my launcher"], ["My PyCharm"]),
                         config.launcher_settings(settings))
        settings["pycharm"]["default_path"] = "../outside"
        with self.assertRaises(ValueError):
            config.launcher_settings(settings)


if __name__ == "__main__":
    unittest.main()

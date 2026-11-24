# Tools

Utilities for maintaining and opening this repository. Run the following commands from the repository root.

## Markdown-to-notebook converter

[`markdown_to_notebooks.py`](markdown_to_notebooks.py) creates missing notebooks alongside Markdown files in the configured `software/python` reference sections. Python fenced blocks become code cells; other content remains in Markdown cells. Existing notebooks are never overwritten, but are checked against their Markdown sources.

```bash
uv run --no-project tools/markdown_to_notebooks.py
```

To check pairs without creating files:

```bash
uv run --no-project tools/markdown_to_notebooks.py --check
```

The converter reports missing or mismatched notebooks and filename collisions. Notebook examples are not executed. Run its tests with:

```bash
uv run --no-project tools/test_markdown_to_notebooks.py
```

## PyCharm launcher

[`open_k_m_s_in_pycharm.sh`](open_k_m_s_in_pycharm.sh) opens the repository root in PyCharm, or a directory specified relative to the repository root. It uses a PyCharm command-line launcher if available, with a macOS application fallback.

```bash
bash tools/open_k_m_s_in_pycharm.sh
bash tools/open_k_m_s_in_pycharm.sh software/pycharm
```
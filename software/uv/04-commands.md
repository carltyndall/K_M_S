# uv Commands & Shortcuts

## Project & Dependency Management
- `uv init`: Initialize a new Python project with a `pyproject.toml`.
- `uv add <package>`: Add a dependency to `pyproject.toml` and update the lockfile.
- `uv remove <package>`: Remove a dependency from the project.
- `uv lock`: Generate or update the `uv.lock` lockfile.
- `uv sync`: Sync the project virtual environment with `uv.lock`.
- `uv tree`: Display the project dependency tree.
- `uv export`: Export lockfile dependencies to `requirements.txt` format.

## Execution & Script Running
- `uv run <command>`: Execute a command or script within the project environment.
- `uv run --python <version> <script.py>`: Run a script using a specific Python version on the fly.
- `uv tool run <tool>` / `uvx <tool>`: Execute an isolated CLI tool without permanent installation (e.g., `uvx ruff check .`).
- `uv tool install <tool>`: Install a standalone CLI tool globally into its own isolated environment.
- `uv tool list`: List all globally installed CLI tools.

## Python Version Management
- `uv python install <version>`: Download and install a specific CPython or PyPy version (e.g., `uv python install 3.12 3.13 3.14`).
- `uv python list`: List available and installed Python versions.
- `uv python find`: Locate the active Python binary.
- `uv python pin <version>`: Pin the Python version for the current directory in `.python-version`.

## Pip Compatibility Interface
- `uv pip install <package>`: High-speed drop-in replacement for `pip install`.
- `uv pip list`: List packages installed in the active environment.
- `uv pip compile requirements.in -o requirements.txt`: Fast dependency resolution and compilation.
- `uv pip sync requirements.txt`: Synchronize the active environment exactly with a requirements file.

## Environment & Cache Management
- `uv venv [path]`: Create a fast virtual environment at the target path.
- `uv cache clean`: Remove all cached wheels and source distributions.
- `uv cache prune`: Prune expired or unused items from the cache.

## GUI Shortcuts
- N/A: uv is a high-performance command-line tool.

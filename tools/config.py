"""Load settings shared by the repository maintenance tools."""

import shlex
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config.toml"


def load_config(path=CONFIG):
    with path.open("rb") as file:
        return tomllib.load(file)


def string_list(value, name):
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise ValueError(f"{name} must be a list of non-empty strings")
    return value


def relative_path(value, name):
    if not isinstance(value, str) or not value or Path(value).is_absolute() or ".." in Path(value).parts:
        raise ValueError(f"{name} must be a non-empty path relative to the repository root")
    return value


def launcher_settings(config):
    settings = config["pycharm"]
    default = relative_path(settings["default_path"], "pycharm.default_path")
    cli = string_list(settings["cli_launchers"], "pycharm.cli_launchers")
    apps = string_list(settings["macos_apps"], "pycharm.macos_apps")
    return default, cli, apps


if __name__ == "__main__":
    try:
        default, cli, apps = launcher_settings(load_config())
        print(f"DEFAULT_PATH={shlex.quote(default)}")
        print("CLI_LAUNCHERS=(" + " ".join(map(shlex.quote, cli)) + ")")
        print("MACOS_APPS=(" + " ".join(map(shlex.quote, apps)) + ")")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"error loading {CONFIG}: {error}", file=sys.stderr)
        sys.exit(1)
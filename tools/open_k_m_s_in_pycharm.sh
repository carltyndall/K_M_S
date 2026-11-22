#!/usr/bin/env bash
# Open this KMS repository as a PyCharm project from the shell.
# Paths are resolved from this script (KMS root = parent of tools/).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KMS_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

usage() {
  cat <<'EOF'
Usage: tools/open_kms_in_pycharm.sh [path]

Open the KMS PyCharm project (default: repository root).
Optional path must be relative to the KMS root.

Examples:
  ./tools/open_kms_in_pycharm.sh
  ./tools/open_kms_in_pycharm.sh software/pycharm
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

TARGET="${KMS_ROOT}"
if [[ $# -ge 1 ]]; then
  ARG="$1"
  if [[ "${ARG}" == /* ]]; then
    echo "error: absolute paths are not used; pass a path relative to the KMS root" >&2
    exit 1
  fi
  TARGET="${KMS_ROOT}/${ARG}"
fi

if [[ ! -d "${TARGET}" ]]; then
  echo "error: not a directory: ${TARGET}" >&2
  exit 1
fi

launch_with_cli() {
  local bin="$1"
  if command -v "${bin}" >/dev/null 2>&1; then
    "${bin}" "${TARGET}"
    return 0
  fi
  return 1
}

# Prefer JetBrains CLI launchers (Toolbox / IDE generated), then macOS open.
if launch_with_cli pycharm; then
  exit 0
fi
if launch_with_cli charm; then
  exit 0
fi
if launch_with_cli pycharm64.exe; then
  exit 0
fi

if [[ "$(uname -s)" == "Darwin" ]]; then
  for app in "PyCharm" "PyCharm CE" "PyCharm Professional"; do
    if open -na "${app}" --args "${TARGET}" 2>/dev/null; then
      exit 0
    fi
  done
fi

echo "error: PyCharm CLI not found. Install a command-line launcher from" >&2
echo "  PyCharm → Tools → Create Command-line Launcher…  (or JetBrains Toolbox)" >&2
echo "On macOS you can also install the app so 'open -a PyCharm' works." >&2
exit 1

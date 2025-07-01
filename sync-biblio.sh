#!/usr/bin/env bash
set -euo pipefail

md="$1"

# Find the user’s HOME — always works on macOS
USER_HOME="$HOME"

SCRIPT_PATH="$USER_HOME/sync_biblio/scriv_sync/main.py"

# Path to Python — try brew python3, fallback to system python3
if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3)"
else
  echo "❌ Python3 not found. Install Python 3 to run the sync script."
  exit 1
fi

"$PYTHON_BIN" "$SCRIPT_PATH" "$md"
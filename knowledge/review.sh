#!/bin/bash
# Clinician review wrapper — handles venv, callable from repo root.
# Usage: bash knowledge/review.sh "clinical question" [--condition "name"] [--json]
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/.venv/bin/python3" "$SCRIPT_DIR/clinician_review.py" "$@"

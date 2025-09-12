#!/usr/bin/env bash
set -e
echo "== GCZA Linux Check =="
node -v || echo "Node fehlt (empfohlen: v20 LTS)."
python3 --version || echo "Python 3.11 empfohlen."
docker --version
python3 OPS/scripts/validate_registry.py || true
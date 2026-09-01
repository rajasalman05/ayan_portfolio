#!/usr/bin/env bash
set -o errexit

# Force pip to bypass PEP 668 externally managed environment restriction
python3 -m pip install --break-system-packages --user -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input
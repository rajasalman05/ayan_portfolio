#!/usr/bin/env bash
set -o errexit

# Install dependencies using --break-system-packages flag for Vercel's Python environment
python3 -m pip install --break-system-packages -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input
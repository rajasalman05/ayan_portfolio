#!/usr/bin/env bash
set -o errexit

# Install requirements
python3 -m pip install --break-system-packages --user -r requirements.txt

# Collect static files explicitly
python3 manage.py collectstatic --no-input --clear
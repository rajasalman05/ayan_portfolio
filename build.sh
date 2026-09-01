#!/usr/bin/env bash
set -o errexit

# Add user bin to PATH
export PATH=$PATH:/vercel/.local/bin

# Install requirements
python3 -m pip install --break-system-packages --user -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input
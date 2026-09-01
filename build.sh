#!/usr/bin/env bash
set -o errexit

# Create and activate virtual environment to bypass PEP 668 / uv managed environment error
python3 -m venv .venv
source .venv/bin/activate

# Install requirements inside venv
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input
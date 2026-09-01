#!/usr/bin/env bash
set -o errexit

# Install dependencies in standard global environment inside Vercel container
pip install -r requirements.txt

# Run collectstatic to generate staticfiles folder
python manage.py collectstatic --no-input --clear
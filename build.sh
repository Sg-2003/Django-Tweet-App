#!/usr/bin/env bash
# Build script for Render deployment
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python chaiwala/manage.py collectstatic --no-input

# Apply database migrations
python chaiwala/manage.py migrate

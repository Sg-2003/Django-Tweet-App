#!/usr/bin/env bash
# Build script for Render deployment
set -o errexit

# Collect static files
python chaiwala/manage.py collectstatic --no-input

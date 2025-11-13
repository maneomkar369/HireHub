#!/bin/bash

# Build script for Vercel deployment
pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

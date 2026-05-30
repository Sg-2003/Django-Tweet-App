import os
import sys

# Add the chaiwala project directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'chaiwala'))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chaiwala.settings')

# Import the Django WSGI application
from chaiwala.wsgi import application

# Vercel expects a variable named `app`
app = application

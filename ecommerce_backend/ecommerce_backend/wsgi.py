"""
WSGI config for ecommerce_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import sys
import os

# Add your project directory to the sys.path
sys.path.append('/home/roridaniel/alx-project-nexus/ecommerce_backend/')

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce_backend.settings'

# Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

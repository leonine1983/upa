"""
WSGI config for upa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upa.settings')

load_dotenv()

application = get_wsgi_application()

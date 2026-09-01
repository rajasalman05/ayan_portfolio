"""
WSGI config for ayan_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayan_portfolio.settings')

# Base WSGI Application
base_application = get_wsgi_application()

# Vercel Serverless Environment ke liye Direct WhiteNoise Wrapper
# 'app' aur 'application' dono variables expose kar rahe hain taake Vercel auto-detect kar le
application = WhiteNoise(base_application, root=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles'))
app = application
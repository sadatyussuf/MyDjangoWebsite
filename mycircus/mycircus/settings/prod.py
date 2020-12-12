import os  
from .base import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  


DEBUG = False

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")






from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    #MySQL Database
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u424564495_PruebasDjango',
        'USER': 'u424564495_DavidPalacios',
        'PASSWORD': 'DavidPalacios123',
        'HOST': 'sql396.main-hosting.eu',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'


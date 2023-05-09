import os

from distutils.util import strtobool
from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APPEND_SLASH = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv("DEBUG", "1")))

# SECURITY WARNING: don't run with all hosts allowed in production!
allowed_hosts = os.getenv("ALLOWED_HOSTS", "*")
ALLOWED_HOSTS = list(map(str.strip, allowed_hosts.split(",")))

# SECURITY WARNING: don't run with permissions disabled in production!
PERMISSIONS_DISABLED = bool(strtobool(os.getenv("PERMISSIONS_DISABLED", "1")))


# Applications
BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.shared",
    "apps.users",
    "apps.students",
    "apps.teachers",
    "apps.schools",
    "apps.subjects",
    "apps.authentication",
    "apps.requests",
    "apps.homeworks",
    "apps.calendar",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "knox",
    "django_rest_passwordreset",
    "simple_history",
    "drf_yasg",  # swagger
    "corsheaders",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_PARTY_APPS


# Third party apps settings
SWAGGER_SETTINGS = {
    "DOC_EXPANSION": "none",
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
}

REST_KNOX = {
    "TOKEN_TTL": timedelta(days=int(os.getenv("KNOX_TOKEN_TTL_DAYS", "365"))),
    "TOKEN_LIMIT_PER_USER": None,
    "AUTO_REFRESH": bool(strtobool(os.getenv("KNOX_AUTO_REFRESH", "1"))),
}

DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME = int(
    os.getenv("MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME", "24")
)
DJANGO_REST_MULTITOKENAUTH_REQUIRE_USABLE_PASSWORD = False

GOOGLE_CALENDAR_PATH_TO_GOOGLE_CREDENTIALS = os.path.join(
    BASE_DIR, "google-credentials.json"
)
GOOGLE_CALENDAR_PATH_TO_TOKEN = os.path.join(BASE_DIR, "token.json")
GOOGLE_CALENDAR_SCOPES = ["https://www.googleapis.com/auth/calendar"]


# Middleware
MIDDLEWARE = [
    # CORS
    "corsheaders.middleware.CorsMiddleware",
    # Django default
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # simple history
    "simple_history.middleware.HistoryRequestMiddleware",
]


ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "config.wsgi.application"


AUTH_USER_MODEL = "users.User"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "db"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")


# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_URL,
    }
}


# Email
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR, "static")
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS ALLOWED ORIGINS
# ALLOW ALL ORIGINS
CORS_ORIGIN_ALLOW_ALL = True

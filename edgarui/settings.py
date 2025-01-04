import logging
import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

# when running in Cloud Run, the filesystem of the application is read-only
# so loading .env from current directory won't work.
# So we mount the secret, which contains an env file, in a fixed path
secret_mounted_env = "/secrets/app_config.env"
if os.path.exists(secret_mounted_env) and os.access(secret_mounted_env, os.R_OK):
    load_dotenv(secret_mounted_env)
    logging.info(f"Loading environment variables from {secret_mounted_env}")
else:
    load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
devkey = "django-insecure-n%*4w3x+b!=709@2jj_=6soqd4afl+#)666hi_fb+tn3&%t(xa"
SECRET_KEY = os.environ.get("SECRET_KEY", devkey)
ALLOWED_HOSTS = [".localhost", "127.0.0.1", ".run.app"]
CSRF_TRUSTED_ORIGINS = ["https://*.run.app", "http://localhost:8000"]
DEBUG = os.getenv("DEBUG", "0") == "1"

# in Cloud Run, the current directory is read-only, so we need to
# use another directory for database and staticfiles
WORK_DIR = Path("/tmp") if os.environ.get("K_SERVICE") else BASE_DIR

# Configure logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "formatters": {
            "standard": {
                "format": "[%(levelname)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S %z",
            }
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.environ.get("LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "edgar_explorer",
    "django_tables2",
    "allauth",
    "allauth.account",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "edgarui.urls"

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

WSGI_APPLICATION = "edgarui.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": WORK_DIR / "edgarui.db",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
STATIC_ROOT = WORK_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Allauth settings
ACCOUNT_ADAPTER = "edgarui.adapters.NoSignupAdapter"
ACCOUNT_LOGOUT_ON_GET = True

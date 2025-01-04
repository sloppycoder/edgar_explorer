# various changes to settings.py
This file documents changes made for implementing allauth, whitenoiss.

## generic app specific settings
```python
# <project>/settings.py

# these are usually at the almost top of the file

from dotenv import load_dotenv
# when running in Cloud Run, the filesystem of the application is read-only
# so loading .env from current directory won't work.
# So we mount the secret, which contains an env file, in a fixed path
secret_mounted_env = "/secrets/app_config.env"
if os.path.exists(secret_mounted_env) and os.access(secret_mounted_env, os.R_OK):
    load_dotenv(secret_mounted_env)
    logging.info(f"Loading environment variables from {secret_mounted_env}")
else:
    load_dotenv()

devkey = "insecure"
SECRET_KEY = os.environ.get("SECRET_KEY", devkey)
ALLOWED_HOSTS = [".localhost", "127.0.0.1", ".run.app"]
CSRF_TRUSTED_ORIGINS = ["https://*.run.app", "http://localhost:8000"]
DEBUG = os.getenv("DEBUG", "0") == "1"

# in Cloud Run, the current directory is read-only, so we need to
# use another directory for database and staticfiles
WORK_DIR = Path("/tmp") if os.environ.get("K_SERVICE") else BASE_DIR

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
```

## Use whitenoise to service static files
Use whitenoise to serve static files. Used for deploying the app without a web server, e.g. in Google Cloud Run or low volume local apps.

```python

# <project>/settings.py

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

STATIC_ROOT = BASE_DIR / "staticfiles" # or use WORK_DIR if running in Cloud Run
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

```

Create ```STATIC_ROOT`` directory and run the following command to collect static files to be served

```shell

python manage.py collectstatic --no-input


## Authentication
Use ```django-allauth``` to implement authentication.


```python
# <project>/settings.py

INSTALLED_APPS = [
    "allauth",
    "allauth.account",
]

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# disable Signup, see adapter code below
ACCOUNT_ADAPTER = "edgarui.adapters.NoSignupAdapter"
ACCOUNT_LOGOUT_ON_GET = True

# <project>/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class NoSignupAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        # Always return False to disable signup
        return False

```

To customize the login screen, create a html template to override the default one.
```shell
cd <app>
mkdir -p templates/account
cp <your_html_template> templates/account/login.html

```

To disable the messages when sign in and sign out, create 2 empty files as message templates. this will override existing templates, and eliminate messages.

```shell

cd <app>
mkdir -p templates/account/messages
touch templates/account/messages/logged_in.txt
touch templates/account/messages/logged_out.txt

```

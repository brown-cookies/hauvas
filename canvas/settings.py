import dj_database_url
import datetime
from dotenv import load_dotenv
from enum import Enum
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ENVIRONMENT OPTIONS
class Env(Enum):
    LOCAL = "local"
    PRODUCTION = "production"
    STAGING = "staging"
    TESTING = "testing"


# loading .env files
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("APP_DEBUG")) or True

# Config that specifies the current environment the application is running in.
# local: Used for local development. (default)
# production: Used when the application is deployed in a live environment.
# staging: Used for testing changes before deploying them to production.
# testing: Used for running automated tests.
ENVIRONMENT = os.getenv("APP_ENV") or "local"

CORS_REPLACE_HTTPS_REFERRER = False
HOST_SCHEME = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HOSTS_SECONDS = None
SECURE_HOSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    os.getenv("APP_KEY")
    if not DEBUG
    else "django-insecure-b(3e8wi+f29*3dvi0+p6dqan%!g)zau=w+8tl#g6xw37wwx5re"
)

ALLOWED_HOSTS = [".herokuapp.com"] if DEBUG else [os.getenv("APP_URL")]

INTERNAL_IPS = ["127.0.0.1"]

# Application definition
INSTALLED_APPS = [
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "grappelli.dashboard",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "debug_toolbar",
    "django_components",
    "django_seed",
    # "haystack",
    "rest_framework",
    "storages",
    "dashboard",
    "canvas",
    "main",
    "announcement",
    "grade",
    "inbox",
    "todo",
    "event",
    "api",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "canvas.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "django_components.templatetags.component_tags",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                        "django_components.template_loader.Loader",
                    ],
                )
            ],
        },
    },
]

# HAYSTACK_CONNECTIONS = {
#     "default": {
#         "ENGINE": "haystack.backends.solr_backend.SolrEngine",
#         "URL": "http://127.0.0.1:8983/solr",
#     },
# }

WSGI_APPLICATION = "canvas.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# db_from_env = dj_database_url()
# DATABASES["default"].update(db_from_env)
# DATABASES["default"]["CONN_MAX_AGE"] = 500

# Use production database
# if not DEBUG and ENVIRONMENT == Env.PRODUCTION:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "OPTIONS": {
#                 "service": "my_service",
#                 "passfile": ".my_pgpass",
#             },
#         }
#     }


#  Message Storage
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Session
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Save session on every request (to keep persistency)
SESSION_SAVE_EVERY_REQUEST = True

# Session Default Age (Default = 7 Days)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# Use secure cookies if you are on HTTPS
SESSION_COOKIE_SECURE = True

# HttpOnly flag to prevent JavaScript access to the session cookie
SESSION_COOKIE_HTTPONLY = True

# Optionally set the cookie's SameSite attribute
SESSION_COOKIE_SAMESITE = "Lax"  # or 'Strict', 'None' depending on your requirements

# Login / Logout URL (Using URL Namespace Path login=hostname/login/)
LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = "login"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_DIRS = [BASE_DIR / "static_my_project", BASE_DIR / "components"]
STATIC_URL = "static_my_project/"
STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media_root")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# AWS Configuration
AWS_GROUP_NAME = os.getenv("AWS_GROUP_NAME")
AWS_USERNAME = os.getenv("AWS_USERNAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "cpe-hauvas-bucket"
AWS_S3_SIGNATURE_NAME = ("s3v4",)
AWS_S3_REGION_NAME = "ap-southeast-2"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
# DEFAULT_FILE_STORAGE = "canvas.aws.utils.MediaRootS3BotoStorage"
# STATICFILES_STORAGE = "canvas.aws.utils.StaticRootS3BotoStorage"

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3boto3.S3StaticStorage"},
    "staticfiles": {"BACKEND": "storages.backends.s3boto3.S3StaticStorage"},
}


if ENVIRONMENT == "production":
    S3_URL = f"//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"
    STATIC_ROOT = S3_URL
    STATIC_URL = S3_URL + "static/"
    MEDIA_URL = f"//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/"
    MEDIA_ROOT = MEDIA_URL
    ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

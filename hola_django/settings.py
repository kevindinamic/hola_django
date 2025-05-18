from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-llave-falsa"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "home",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "hola_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [],
        },
    },
]

WSGI_APPLICATION = "hola_django.wsgi.application"

STATIC_URL = "/static/"

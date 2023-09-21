#base settings that dev and prod will build upon 

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",    
]

CUSTOM_APPS = [
    "apps.user",
    "apps.resources",
    "apps.core",
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = [*DEFAULT_APPS, *CUSTOM_APPS, *THIRD_PARTY_APPS]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middleware.log.simple_logging_middleware",
    #"apps.core.middleware.logging.ViewExecutionTimeMiddleware2"
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "templates")],
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR / "static")]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'user.User'
LOGIN_URL = "login"

# Logger configuration
LOGGING = {
    'version': 1, #dictConfig format version is wohl egal
    'loggers': {
            'logging_mw': { #specify the logger instance we created
                'handlers': ['file', 'console'], #decide which handler to handle it
                'level': 'DEBUG' #specifies the minimum level for this handler to do stuff
            }     
        },
    'handlers': {
        "console": { #name of handler
            'level': 'DEBUG', # handle this logging level and all above it
            'class': 'logging.StreamHandler', # Defines the medium to send the logs
            'filters': ['only_if_debug_true'] #handle only if DEBUG=True in settings
        },
        "file": { #name of handler
            'level': 'INFO', # handle this logging level and all above it
            'class': 'logging.FileHandler', # Defines the medium to send the logs
            'filename': str(BASE_DIR / "logs" / "req_res_logs.txt"),
            'formatter': 'verbose',
            }
        },
    'formatters': {
        'verbose': { #name of formatter
            'format': '{levelname} {asctime} {module} :: {message}', #levelname gives log level, asctime gives time of (), module gives name of module log came from
            'style': "{", #clarifies i used curly braces to access attributes
        }
    },
    'filters': {
        "only_if_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
}
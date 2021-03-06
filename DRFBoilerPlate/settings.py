"""
Django settings for DRFBoilerPlate project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'default')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost',
'127.0.0.1',
 #HOST_IP
 #HOST_NAME
 'subdomain.domain.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     #custom
    'customauth',
    'content',
    'rest_framework',
    #Thirds
    'corsheaders',
    'django_rest_passwordreset',
    'knox',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
       'https://subdomain.domain.com:443',
       'https://subdomain.domain.com:443',
       'https://domain.com:443',
       'https://subdomain.domain.com',
       'https://subdomain.domain.com',
       'https://domain.com',
       'http://subdomain.domain.com:443',
       'http://domain.com:443',
       'http://subdomain.domain.com',
       'http://domain.com',
       'http://127.0.0.1:443',
       'http://127.0.0.1:3000',
       'https://127.0.0.1:443',
    #    'https://IP:443',
    #    'https://IP',
    #    'http://IP',
       'https://127.0.0.1:3000',
       'http://127.0.0.1:8000',
       'http://127.0.0.1',
)

#Sessiones
CSRF_TRUSTED_ORIGINS = [
    'subdomain.domain.com',
    'subdomain.domain.com/*',
    'domain.com',
    '127.0.0.1',
    ]

ALLOWED_IP=[
    '127.0.0.1',
    'localhost',
    # 'IP',
    # 'IP:443'
]

DCS_SESSION_COOKIE_SAMESITE = None
DCS_SESSION_COOKIE_SAMESITE_FORCE_CORE = False
DCS_SESSION_COOKIE_SAMESITE_FORCE_ALL = True


ROOT_URLCONF = 'DRFBoilerPlate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DRFBoilerPlate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
  'default': {
    # MySQL engine. Powered by the mysqlclient module.
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get('DB_NAME', 'default'),
    'USER': os.environ.get('DB_USER', 'default'),
    'PASSWORD': os.environ.get('DB_PASS', 'default'),
    'HOST': os.environ.get('DB_HOST', 'default'),
    'PORT': os.environ.get('DB_PORT', 'default'),
  }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "customauth.CustomUser"


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/user/api.domain.com/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/user/api.domain.com/media'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'default')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 'default')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'default')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'default')
EMAIL_USE_TLS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ensures that requests over HTTP are redirected to HTTPS
SECURE_SSL_REDIRECT = True

# Tells browser to only send cookies over HTTPS
SESSION_COOKIE_SECURE = True

# Prevents cross site request forgery attacks
CSRF_COOKIE_SECURE = True
import os
from pathlib import Path
from django.contrib.messages import constants
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-qlcrg0+9a-5k5ppo1*k53ad9fj(f^99afa^!ywl6s-g%n%zzxp'
SECRET_KEY = os.environ.get('SECRET_KEY', 'INSECURE')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True if os.environ.get('DEBUG') == '1' else False
DEBUG = False 

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    "http://34.176.141.229",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    #restrição por grupo  'django_group_role', 'guardian'
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Access_Login',
    'Atendimento',
    'Triagem',
    'Medicos',
    'utils',
    'websocket_app',
    'django.contrib.humanize',
    'configUPA',
    'PrintPDFs',
    'ckeditor'   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # SessionMiddleware é o responsável gerenciar as sessões de usuarios
    'django.contrib.sessions.middleware.SessionMiddleware',  
    # ---------------------------------------------------------- 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#Trecho configurado para usar o armazenamento de sessão em cache
#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# --------------------------------------------------------------

ROOT_URLCONF = 'upa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base_templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'utils.context_processors.grupo_usuario',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'upa.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'base_static',
    BASE_DIR / 'media'
]
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# MINHAS CONFIGURAÇÕES EXTRAS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Adicione o tipo MIME correto para arquivos JS

import mimetypes
mimetypes.add_type("text/javascript", ".js", True)


# Security settings
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# Message settings
MESSAGE_TAGS = {
    constants.DEBUG: 'alert-secondary',
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',
    constants.ERROR: 'alert-danger',
}

# DEFINIÇÕES DE SEGURANÇA PARA SESSÕES. 

# 1º define o mecanismo de armazenamento de sessão para 'django.contrib.sessions.backends.cache' ou
# o 'django.contrib.sessions.backends.db' conforme a preferência. Foi escolhido armazenamento em cache
SESSION_ENGINE =   'django.contrib.sessions.backends.cache'

# 2º define a chave de assinatura da sessão
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# 3º Define o tempo de sessão para 1 hora (3600 segundos)
#SESSION_COOKIE_AGE = 3600

# Por fim definir a pagina para onde será redirecionada o usuario apos finalizar a sessão
LOGIN_URL = 'Access_Login:access_login_page'

"""
# Define o tempo de sessão para 1 hora (3600 segundos)
#SESSION_COOKIE_AGE = 3600

"""
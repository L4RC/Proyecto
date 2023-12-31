"""
Django settings for pagina project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cs+dc9$75+7%_n3933rdihl(94d08v&2!*nk)$=y6yzldh)*1x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #en local es true, en servidor es false

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
     'jazzmin',#se agrego
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ppaginas',# se agrego
    'cursos',#se agrego
    'estudiante', #se agrego
    'docente', #se agrego
    'asignacion',
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pagina.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
 #               'carro.context_processor.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'pagina.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {  #Conexión a base de datos
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'academia',
        'USER' : 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'DATABASE_PORT' : '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#MEDIA_URL = '/media/' #carpeta de media
#MEDIA_ROOT= Path.join(BASE_DIR,'media')

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" #lineas para el correo 
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "estudianteusac54@gmail.com"#agregar el correo
EMAIL_HOST_PASSWORD = ""   #agregar la contraseña

CRISPY_ALLOWED_TEMPLATE_PACK = "botstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4" 

LOGIN_REDIRECT_URL = reverse_lazy('Estudiante')
LOGOUT_REDIRECT_URL = 'Inicio'  # Reemplaza 'inicio' con la URL de tu página de inicio

#LOGIN_URL = 'accounts:login'  # Reemplaza 'accounts:login' con la ruta correcta a tu vista de inicio de sesión

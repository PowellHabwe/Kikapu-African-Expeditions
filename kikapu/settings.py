"""
Django settings for kikapu project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4x+z9%@z!95*prknyz_$8s(p1199)iy$30ex%j50r2w+7elmt_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS=['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'crispy_forms',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'accounts',
    # 'whitenoise.runserver_nostatic',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kikapu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':['templates'],
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

WSGI_APPLICATION = 'kikapu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'ww456205@gmail.com'
EMAIL_HOST_PASSWORD = 'Affir6mative'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# sudo apt update
# sudo apt upgrade

# sudo apt install python3-pip python3-dev nginx

# pip install --upgrade pip
# python3 venv -m kikapu_env

# mkdir -p /webapps/kikapu/
# cd /webapps/kikapu/

# sudo groupadd --system webapps

# sudo useradd --system --gid webapps --shell /bin/bash --home /webapps/kikapu kikapu

# pip install -r requirements.txt

# python -m venv kikapu_env

# source kikapu_env/bin/activate

# sudo mv Kikapu-African-Expeditions kikapu



#  python3 -m venv /root/env/kikapu
# sudo nano /etc/nginx/sites-available/aspirecbo.conf
# sudo ln -s /etc/nginx/sites-available/kikapu.conf /etc/nginx/sites-enabled/
# Upstream configuration


# the upstream component nginx needs to connect to
# Update your Nginx configuration file (/etc/nginx/sites-available/kikapu.conf) with the following content:

# perl
# Copy code
# server {
#     listen 80;
#     server_name aspire.co.ke www.aspire.co.ke;
#     charset utf-8;

#     location / {
#         proxy_pass http://127.0.0.1:8000;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header X-Forwarded-Proto $scheme;
#     }
# }



#

#!/usr/bin/env bash

# NAME='kikapu'
# DJANGODIR=/webapps/kikapu/kikapu
# SOCKFILE=/webapps/kikapu/run/gunicorn.sock
# USER=kikapu
# GROUP=webapps
# NUM_WORKERS=3
# DJANGO_SETTINGS_MODULE=kikapu.settings
# DJANGO_WSGI_MODULE=kikapu.wsgi
# TIMEOUT=120

# cd $DJANGODIR
# source /webapps/kikapu/kikapu_env/bin/activate
# export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
# export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# RUNDIR=$(dirname $SOCKFILE)

# test -d $RUNDIR || mkdir -p $RUNDIR

# exec /webapps/kikapu/kikapu_env/bin/gunicorn ${DJANGO_WSGI_MODULE}.application \
# --name $NAME \
# --workers $NUM_WORKERS \
# --timeout $TIMEOUT \
# --user=$USER \
# --group=$GROUP \
# --bind=unix:$SOCKFILE \
# --log-level=debug \
# --log-file=-


# chmod +x ./kikapu_env/bin/gunicorn_start
# chown - R kikapu:webapps .
# ls -larth


# [program:kikapu]
# command = /webapps/kikapu/kikapu_env/bin/gunicorn_start
# user = kikapu
# stdout_logfile = /webapps/kikapu/logs/supervisor.log
# redirect_stderr = true
# environment = LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8

# upstream kikapu_web_server {
#     server unix:/webapps/kikapu/run/gunicorn.sock fail_timeout=0;
# }

# server {
#     listen 80;
#     server_name kikapu.com;

#     access_log /webapps/kikapu/logs/access.log;
#     error_log /webapps/kikapu/logs/error.log;

#     location /static/ {
#         alias /webapps/kikapu/kikapu/static/;
#     }

#     location /media/ {
#         alias /webapps/kikapu/kikapu/media/;
#     }

#     location / {
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header Host $http_host;
#         proxy_redirect off;

#         if (!-f $request_filename) {
#             proxy_pass http://kikapu_web_server
#         }
#     }
# }


# server {
#     listen 80;
#     server_name 64.23.163.87;  # Use your server's IP address or hostname

#     location = /favicon.ico { access_log off; log_not_found off; }

#     location /static/ {
#         alias /webapps/kikapu/kikapu/articles/static/;
#     }

#     location /media/ {
#         alias /webapps/kikapu/media/;
#     }

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/webapps/kikapu/run/gunicorn.sock;
#     }
# }


#  {% extends 'base_layout.html' %}
# {% load static %}

# {% block content %}


# <section class="bg0">
# 	<div class="container">
# 		<div class="row m-rl--1">
# 			<div class="col-sm-6 col-lg-4 p-rl-1 p-b-2">
# 				<a href="{% static 'articles/images/post-01.jpg' %}" class="dis-block how1-child1 trans-03"></a>
# 				<div class="bg-img1 size-a-12 how1 pos-relative"
# 					style="background-image: url({% static 'articles/images/post-01.jpg' %});"></div>
# 			</div>

# 			<div class="col-sm-6 col-lg-4 p-rl-1 p-b-2">
# 				<a href="{% static 'articles/images/post-02.jpg' %}" class="dis-block how1-child1 trans-03"></a>
# 				<div class="bg-img1 size-a-12 how1 pos-relative"
# 					style="background-image: url({% static 'articles/images/post-02.jpg' %});"></div>
# 			</div>


# 		</div>
# 	</div>
# </section>



# {% endblock %} 




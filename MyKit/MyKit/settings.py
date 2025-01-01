"""
Django settings for MyKit project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import json

import chardet

# 获取项目根路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 获取项目配置文件 config.json 的编码格式
with open(os.path.join(BASE_DIR, "config", "config.json"), "rb") as store_file:
    raw_data = store_file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# 获取项目配置文件 config.json，并读取相关参数
with open(os.path.join(BASE_DIR, "config", "config.json"), "r", encoding=encoding) as store_file:
    STORED = json.load(store_file)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = STORED['KEY']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # 允许其他来源的访问

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'home',         # 主页APP -- 首页，登陆，跳转其他功能页
    'accounting'    # 账单APP -- 简单记账功能 2024-11
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

ROOT_URLCONF = 'MyKit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'MyKit.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': STORED['database']['db_name'],
        'USER': STORED['database']['db_user'],
        'PASSWORD': STORED['database']['db_pw'],
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# LOGIN_URL = 'accounting:login'  # 未登录重定向至登录页面
LOGIN_REDIRECT_URL = 'accounting/'  # 登录成功后重定向到主页或其他页面
LOGOUT_REDIRECT_URL = 'logout'  # 登出后重定向

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# 当您在Django中定义一个没有指定主键的model时，Django将自动为您创建一个主键。
# BigAutoField 为大整型自增字段，比AutoField更适合用于大量记录的场景。
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

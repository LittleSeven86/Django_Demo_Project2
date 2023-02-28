"""
Django settings for Demo1_1 project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g+r7b#*u8wwoxn$oa7a&8&6p@x)&)6c3z56jboftqp!qc0dkf9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'projects.apps.ProjectsConfig',
    'interfaces',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Demo1_1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Demo1_1.wsgi.application'

# 指定在全局配置文件setting.py中的DATAVBASES字典里配置需要连接的数据库信息
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 指定数据库的别名/标签
    # 指定的是Django默认使用的数据库
    'default': {
        # 指定当前使用的数据库引擎
        # django.db.background.mysql\oracle\sqllite3
        'ENGINE': 'django.db.backends.sqlite3',
        # 指定数据库名称，如果使用的是sqllite3，需要指定sqllite3文件的绝对路径
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'NAME':'mydb',
        # 'USER':'root',
        # 'PASSWORD':'123456',
        # 'PORT':3306,
        # 'HOST':'127.0.0.1'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''
20233 0218 DRF中的解析器（类）
    1、可以根据请求头中的Content-Type来自动解析参数，使用统一的data属性来获取即可
    2、默认JSONParser、FormParser、MultiPartParser三个解析器类
        如果需要解析xml Excel参数，可以定义好，直接放到解析器类中使用
    3、可以在全局配置文件（settings.py）中修改DRF全局参数，把REST_FRAMEWORK作为名称
'''
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
            # 'rest_framework.parsers.JSONParser',
            # 'rest_framework.parsers.FormParser',
            # 'rest_framework.parsers.MultiPartParser',
        ],
    '''
    2023 0218 DRF中的渲染器（类）
        1、可以根据请求头中的Accept参数来自动渲染前端需要的数据格式
        2、默认的渲染器为JSONRenderer、BrowsableAPIRenderer
        3、如果前端请求头未指定Accept参数或者指定为application/json，那么会自动返回json格式的数据
        4、如果前端请求头指定Accept参数为text/html，那么默认会返回可浏览的api页面（api进行管理）
        5、可以在DEFAULT_RENDERER_CLASSES中指定需要使用的渲染器
        6、如果想要渲染xml、yaml，定义好渲染器类，在render_class中添加即可
    '''
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 1、在全局DEFAULT_FILTER_BACKENDS指定使用的过滤引擎类（SearchFilter为搜索引擎类）
    # 2、可以在全局使用SEARCH_PARAM修改前端过滤查询字符串参数名称（默认为search）
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter','rest_framework.filters.OrderingFilter'],

    # 'SEARCH_PARAM': 'se',
    # 'ORDERING_PARAM': 'ordering',

    # 1、在全局settings.py文件，DEFAULT_PAGINATION_CLASS上指定分页引擎类PageNumberPagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPagination',
    # 2、指定每一页显示的数据条数
    'PAGE_SIZE': 3,
    # 指定用于支持coreapi的Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}



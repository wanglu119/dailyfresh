#coding=utf-8
"""
Django settings for dailyfresh_23 project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery

REDIS_IP='192.168.0.105'

djcelery.setup_loader()
BROKER_URL = 'redis://%s:6379/4' % REDIS_IP
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sys.path = [
#     '',
#     os.path.join(BASE_DIR, 'apps')
# ]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ez&ql==9z-k(v%kjip9i0+2_i+5dunfp1xxz_+!%sx88*xar3o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    # django用户认证系统的应用,默认使用的
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',  # 富文本编辑器
    'haystack',  # 全文检索
    'djcelery',
    # 'haystack', # 全文检索
    # Django的用户认真系统规定,在注册应用时,应用的名称需要跟 'AUTH_USER_MODEL = 'users.User'' 里面的users保持一致
    'apps.users',
    'apps.goods',
    'apps.orders',
    'apps.cart',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 默认开启了用户认证的验证系统
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dailyfresh_23.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 配置模板加载路径
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

WSGI_APPLICATION = 'dailyfresh_23.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# 更换数据库引擎为MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh_23',
        'HOST': '192.168.0.105', # MySQL数据库地址
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# 配置静态文件加载路径
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 配置Django用户认证系统的模型类,将AbstractUser更换成User
# 说明:django的用户认证系统,只允许一级导包,只有一个 .
AUTH_USER_MODEL = 'users.User'

# 配置Django的第三方邮件服务器参数
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # 导入邮件模块
EMAIL_HOST = 'smtp.yeah.net' # 发邮件主机
EMAIL_PORT = 25 # 发邮件端口
EMAIL_HOST_USER = 'dailyfreshzxc@yeah.net' # 授权的邮箱
EMAIL_HOST_PASSWORD = 'dailyfresh123' # 邮箱授权时获得的密码，非注册登录密码
EMAIL_FROM = '天天生鲜<dailyfreshzxc@yeah.net>' # 发件人抬头


# 缓存 : 搭配django_redis使用的
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:6379/5" % REDIS_IP,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Session
# http://django-redis-chs.readthedocs.io/zh_CN/latest/#session-backend

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 搭配login_required装饰器使用的,当用户未登录时进入的地址
LOGIN_URL = '/users/login'

# 搭配自定义的文件存储系统使用的,指定文件存储到fdfs时,找哪个类来处理
# DEFAULT_FILE_STORAGE = 'utils.fastdfs.storage.FastDFSStorage'
# # 配置client.conf的路径
# CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')
# # 配置nginx的ip
# # SERVER_IP = 'http://192.168.159.131:8888/'
# SERVER_IP = 'http://localhost/'

# 配置富文本编辑器的样式
TINYMCE_DEFAULT_CONFIG = {
  'theme': 'advanced', # 丰富样式
  'width': 600,
  'height': 400,
}

# 配置搜索引擎后端
HAYSTACK_CONNECTIONS = {
  'default': {
      # 使用whoosh引擎：提示，如果不需要使用jieba框架实现分词，就使用whoosh_backend
      'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
      # 索引文件路径 : whoosh_index 相当于新华字典,数据库的数据的索引都在里面
      'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
  }
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 配置对接支付宝
ALIPAY_APPID = '2016091100488082'
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'apps/orders/app_private_key.pem')
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'apps/orders/alipay_public_key.pem')
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'

# 配置对接支付宝
ALIPAY_APPID = '2016082100308405'
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'apps/orders/app_private_key.pem')
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'apps/orders/alipay_public_key.pem')
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'

# 配置读写分离
DATABASES_ROUTERS = ['utils.db_router.MasterSlaveDBRouter']

# 收集静态文件目录
STATIC_ROOT = '/Users/zhangjie/Desktop/static_23'


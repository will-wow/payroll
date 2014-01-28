# Local settings file

DEBUG = True

ADMINS = (
    ('will', 'will@whentheresawill.net'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'modern_website',
        'USER': 'whenther',
        'PASSWORD': 'microblog',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = 'D:\Documents\Code\python\modern-website\static'
MEDIA_ROOT = 'D:\Documents\Code\python\modern-website\media'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ALLOWED_HOSTS = ['*']

SECRET_KEY = '5mhd=tgrqe9r(n5fb^#e%cs0jlt(!zx9u+ry1x0^fm99zie=3y'
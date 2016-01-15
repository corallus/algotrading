try:
    from algotrading.settings import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'algo_5',
        'USER': 'root',
        'PASSWORD': 'muscipula',
        'HOST': 'localhost',
        'PORT': '',
    }
}

TIME = 5

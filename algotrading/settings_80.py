try:
    from algotrading.settings import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'algo_80',
        'USER': 'root',
        'PASSWORD': 'muscipula',
        'HOST': 'localhost',
        'PORT': '',
    }
}

TIME = 80
FILE = '/home/vincent/PycharmProjects/algotrading/export_80.xls'

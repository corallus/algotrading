try:
    from algotrading.settings import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'algo_15',
        'USER': 'root',
        'PASSWORD': 'muscipula',
        'HOST': 'localhost',
        'PORT': '',
    }
}

TIME = 15
FILE = '/home/vincent/PycharmProjects/algotrading/export_15.xls'
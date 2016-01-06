from stock_retrieval.models import Share

__author__ = 'kees'


def shares(request):
    return {'shares': Share.objects.all()}

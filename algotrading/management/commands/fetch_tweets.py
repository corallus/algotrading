from django.core.management.base import BaseCommand
from stock_retrieval.models import Share


class Command(BaseCommand):
    def handle(self, *args, **options):
        for share in Share.objects.all():
            share.get_share_display()
            pass

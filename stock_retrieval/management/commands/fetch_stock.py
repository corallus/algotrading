from django.core.management.base import BaseCommand
from stock_retrieval.utils import fetch


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch()


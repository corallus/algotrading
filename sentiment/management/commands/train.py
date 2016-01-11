from django.core.management.base import BaseCommand
from sentiment import utils


class Command(BaseCommand):
    def handle(self, *args, **options):
        utils.train()

from django.core.management.base import BaseCommand
from sentiment import trainer


class Command(BaseCommand):
    def handle(self, *args, **options):
        trainer.train()


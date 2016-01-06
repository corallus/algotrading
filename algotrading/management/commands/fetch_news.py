from django.core.management.base import BaseCommand
from stock_retrieval.models import Share
from news_retrieval.models import NewsArticle


class Command(BaseCommand):
    def handle(self, *args, **options):
        NewsArticle.fetch()
from django.core.management.base import BaseCommand
import feedparser
from datetime import datetime

from stock_retrieval.models import Share
from news_retrieval.models import NewsArticle
from document.models import Document


class Command(BaseCommand):
    def handle(self, *args, **options):
        for share in Share.objects.all():
            feed = feedparser.parse('http://feeds.finance.yahoo.com/rss/2.0/headline?s=%s&lang=en-US' % share.share)
            for item in feed.entries:
                if not NewsArticle.objects.filter(guid=item.guid).exists():
                    document = Document(share=share)
                    document.save()
                    NewsArticle(document=document, guid=item.guid, title=item.title, link=item.link,
                                description=item.description,
                                published=datetime.strptime(item.published, '%a, %d %b %Y %H:%M:%S %Z')).save()


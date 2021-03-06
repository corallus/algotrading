import feedparser
from dateutil import parser
from bs4 import BeautifulSoup
from django.conf import settings

from stock_retrieval.models import Share
from document.models import Document


def fetch():
    feeds = [
        'https://news.google.com/news?q=%s&output=rss&hl=en',
        'https://www.google.co.uk/finance/company_news?q=%s&output=rss&hl=en'
    ]
    results = False
    for share in Share.objects.all():
        for feed in feeds:
            feed = feedparser.parse(feed % share.share)
            for item in feed.entries:
                if not Document.objects.filter(guid=item.guid).exists():
                    results = True
                    soup = BeautifulSoup(item.description, 'html.parser')
                    text = soup.get_text()
                    soup = BeautifulSoup(item.title, 'html.parser')
                    title = soup.get_text()
                    Document(share=share, text=text, title=title, source=item.link,
                                        published=parser.parse(item.published), guid=item.guid, type='na').save()
    return results

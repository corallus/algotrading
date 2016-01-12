import feedparser
from stock_retrieval.models import Share
from document.models import Document
from django.utils.html import strip_tags
from dateutil import parser


def fetch():
    feeds = [
        'https://news.google.com/news?q=%s&output=rss',
        'https://www.google.co.uk/finance/company_news?q=%s&output=rss'
    ]
    for share in Share.objects.all():
        for feed in feeds:
            feed = feedparser.parse(feed % share.share)
            for item in feed.entries:
                if not Document.objects.filter(guid=item.guid).exists():
                    text = strip_tags(item.description)
                    document = Document(share=share, text=text, title=item.title, source=item.link,
                                        published=parser.parse(item.published), guid=item.guid, type='na')
                    document.save()
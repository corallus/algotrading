from django.views.generic import TemplateView, FormView, ListView
from document.models import Document
from django.core.urlresolvers import reverse_lazy


class NewsArticleList(ListView):
    template_name = 'news_retrieval/index.html'
    model = Document

    def get_queryset(self):
        queryset = super(NewsArticleList, self).get_queryset()
        return queryset.order_by('-published').filter(type='na')

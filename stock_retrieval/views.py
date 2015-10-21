from django.views.generic import FormView, ListView

from .forms import SyncFeedForm
from .models import StockPrice, Stock
from django.core.urlresolvers import reverse_lazy


class StockPriceList(ListView):
    template_name = 'stock_retrieval/index.html'
    model = StockPrice


class SyncFeed(FormView):
    form_class = SyncFeedForm
    success_url = reverse_lazy('stock-retrieval')

    def form_valid(self, form):
        Stock.get_stocks()
        return super(SyncFeed, self).form_valid(form)



from django.views.generic import FormView, ListView

from .forms import SyncFeedForm
from .models import Share, ShareDay
from django.core.urlresolvers import reverse_lazy


class ShareDayList(ListView):
    template_name = 'stock_retrieval/index.html'
    model = ShareDay


class SyncFeed(FormView):
    form_class = SyncFeedForm
    success_url = reverse_lazy('stock-retrieval')

    def form_valid(self, form):
        for share in Share.objects.all():
            share.get_historical()
        return super(SyncFeed, self).form_valid(form)

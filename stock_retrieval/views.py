from django.views.generic import FormView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy

from .forms import SyncFeedForm, CreateShareForm
from .models import Share, ShareDay


class ShareDayList(ListView):
    template_name = 'stock_retrieval/index.html'
    model = ShareDay

    def get_context_data(self, **kwargs):
        context = super(ShareDayList, self).get_context_data(**kwargs)
        context['form'] = CreateShareForm()
        return context


class CreateShareView(CreateView):
    model = Share
    success_url = reverse_lazy('stock-retrieval')

    fields = ['share']


class SyncFeed(FormView):
    form_class = SyncFeedForm
    success_url = reverse_lazy('stock-retrieval')

    def form_valid(self, form):
        for share in Share.objects.all():
            share.get_historical()
        return super(SyncFeed, self).form_valid(form)


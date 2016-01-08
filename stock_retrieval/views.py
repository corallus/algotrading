from django.views.generic import FormView, ListView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import SyncFeedForm, CreateShareForm
from .models import Share, ShareDay, ShareValue


class ShareDayList(ListView):
    template_name = 'stock_retrieval/shareday_list.html'
    model = ShareDay

    def get_context_data(self, **kwargs):
        context = super(ShareDayList, self).get_context_data(**kwargs)
        context['form'] = CreateShareForm()
        return context


class ShareValueList(ListView):
    template_name = 'stock_retrieval/index.html'
    model = ShareValue

    def get_context_data(self, **kwargs):
        context = super(ShareValueList, self).get_context_data(**kwargs)
        context['form'] = CreateShareForm()
        context['object_list'] = ShareValue.objects.order_by('-time')
        return context


class DeleteShareView(DeleteView):
    model = Share
    success_url = reverse_lazy('stock-retrieval')


class CreateShareView(CreateView):
    model = Share
    success_url = reverse_lazy('stock-retrieval')

    fields = ['share']

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy('stock-retrieval'))


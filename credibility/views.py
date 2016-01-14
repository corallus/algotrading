from django.db.models import Max
from django.views.generic import ListView
from credibility.models import CredibilityModel, calculate_hits, calculate_source_correctness, calculate_credibility

__author__ = 'vincent'


class BaseCredibilityView(ListView):
    template_name = 'credibility/credibility.html'
    model = CredibilityModel

    def get_context_data(self, **kwargs):
        context = super(BaseCredibilityView, self).get_context_data(**kwargs)
        context.update(CredibilityModel.objects.aggregate(Max('auth'), Max('source_score'), Max('credibility'),
                                                          Max('incoming')))
        return context


class HITSView(BaseCredibilityView):

    def get(self, request, *args, **kwargs):
        calculate_hits()
        return super(HITSView, self).get(request, *args, **kwargs)


class SourceView(BaseCredibilityView):

    def get(self, request, *args, **kwargs):
        calculate_source_correctness()
        return super(SourceView, self).get(request, *args, **kwargs)


class CredibilityView(BaseCredibilityView):

    def get(self, request, *args, **kwargs):
        calculate_credibility()
        return super(CredibilityView, self).get(request, *args, **kwargs)
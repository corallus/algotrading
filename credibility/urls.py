from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from credibility.views import HITSView, CredibilityView, SourceView

urlpatterns = patterns(
    '',
    url(r'credibility/', CredibilityView.as_view(), name='overall-credibility'),
    url(r'^hits/$', HITSView.as_view(), name='credibility-hits'),
    url(r'^source/$', SourceView.as_view(), name='credibility-source'),
    url(r'^$', TemplateView.as_view(template_name="credibility/index.html"), name='credibility'),
)

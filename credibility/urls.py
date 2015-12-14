from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from credibility.views import HITSView

urlpatterns = patterns(
    '',
    url(r'^hits/$', HITSView.as_view(), name='credibility-hits'),
    url(r'^$', TemplateView.as_view(template_name="credibility/index.html"), name='credibility'),
)

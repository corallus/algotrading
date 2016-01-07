from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from social_retrieval.views import TwitterView, TwitterManualView

urlpatterns = patterns(
    '',
    url(r'^twitter/$', TwitterView.as_view(), name='social-twitter'),
    url(r'^twitter-manual/$', TwitterManualView.as_view(), name='social-twitter-manual'),
    url(r'^$', TemplateView.as_view(template_name="social_retrieval/index.html"), name='social-retrieval'),
)
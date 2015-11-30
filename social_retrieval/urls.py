from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from social_retrieval.views import FacebookView, TwitterView

urlpatterns = patterns(
    '',
    url(r'^facebook/$', FacebookView.as_view(), name='social-facebook'),
    url(r'^twitter/$', TwitterView.as_view(), name='social-twitter'),
    url(r'^$', TemplateView.as_view(template_name="social_retrieval/index.html"), name='social-retrieval'),
)
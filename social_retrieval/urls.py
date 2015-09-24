from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="social_retrieval/index.html"), name='social-retrieval'),
)
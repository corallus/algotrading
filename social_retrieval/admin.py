from django.contrib import admin

# Register your models here.
from social_retrieval.models import Tweet
admin.site.register(Tweet, admin.ModelAdmin)


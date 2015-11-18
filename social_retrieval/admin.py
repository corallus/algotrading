from django.contrib import admin

# Register your models here.
from social_retrieval.models import Tweet, Link

admin.site.register(Tweet, admin.ModelAdmin)
admin.site.register(Link, admin.ModelAdmin)

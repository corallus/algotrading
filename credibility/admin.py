from django.contrib import admin

from credibility.models import CredibilityModel

admin.site.register(CredibilityModel, admin.ModelAdmin)

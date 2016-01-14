from django.contrib import admin

from credibility.models import CredibilityModel, SourceModel

admin.site.register(CredibilityModel, admin.ModelAdmin)
admin.site.register(SourceModel, admin.ModelAdmin)

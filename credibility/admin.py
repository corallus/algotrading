from django.contrib import admin

# Register your models here.
from credibility.models import CredibilityBaseModel, HITS

admin.site.register(CredibilityBaseModel, admin.ModelAdmin)
admin.site.register(HITS, admin.ModelAdmin)

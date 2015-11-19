from django.contrib import admin
from .models import Share, ShareDay


admin.site.register(Share, admin.ModelAdmin)
admin.site.register(ShareDay, admin.ModelAdmin)

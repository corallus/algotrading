from django.contrib import admin

from document.models import Document, Link

admin.site.register(Link, admin.ModelAdmin)
admin.site.register(Document, admin.ModelAdmin)
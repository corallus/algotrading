from django.contrib import admin
from .models import Stock, StockPrice


class StockAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}


admin.site.register(Stock, StockAdmin)
admin.site.register(StockPrice, admin.ModelAdmin)

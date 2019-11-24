from django.contrib import admin
from .models import Portfolio
from .models import Stock
# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'realizedGains')


class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticker', 'buyRate', 'quantity')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Stock, StockAdmin)
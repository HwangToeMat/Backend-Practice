from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('htmuser', 'product', 'quantity', 'register_date')


admin.site.register(Order, OrderAdmin)

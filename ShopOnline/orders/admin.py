from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Order, OrderItem



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address', 'paid', 'created',
                    ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]



admin.site.register(Order, OrderAdmin)

import decimal

from django.contrib import admin
from django.http import HttpRequest
from django.utils.html import mark_safe
from django.db.models.query import QuerySet

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    extra = 0
    model = OrderItem
    readonly_fields = ('product_cost', 'total', 'image')
    fields = ('product', 'quantity', 'product_cost', 'total', 'image')

    @admin.display(description='Image')
    def image(self, order_item: OrderItem) -> str:
        return mark_safe(f'<img src="{order_item.product.image}" style="max-width: 200px; max-height: 200px;" />')

    @admin.display(description='Product Cost')
    def product_cost(self, order_item: OrderItem) -> decimal.Decimal:
        return order_item.product.price


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    list_filter = ('timestamp',)
    list_display_links = ('id', 'user')
    list_display = ('id', 'user', 'timestamp')

    readonly_fields = ('id', 'user', 'timestamp', 'total')

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        # premature optimization FTW
        return super().get_queryset(request).select_related('user').only('id', 'user__username', 'timestamp')

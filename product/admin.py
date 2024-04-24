from django.contrib import admin
from django.utils.html import mark_safe

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'name')
    list_display = ('id', 'name', 'cost', 'updated_at')

    readonly_fields = ('image_tag',)

    @admin.display(description='Cost')
    def cost(self, product: Product) -> str:
        return f'${product.price}'

    @admin.display(description='Image')
    def image_tag(self, product: Product) -> str:
        return mark_safe(f'<img src="{product.image}" style="max-width: 200px; max-height: 200px;" />')

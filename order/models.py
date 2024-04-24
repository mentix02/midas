import decimal

from django.db import models


class Order(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='orders')

    @property
    def total(self) -> decimal.Decimal:
        return sum(item.total for item in self.items.all())

    class Meta:
        ordering = ('-timestamp',)


class OrderItem(models.Model):

    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='order_items')

    @property
    def total(self) -> decimal.Decimal:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f'{self.order} - {self.product}'

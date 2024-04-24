import decimal

from django.db import models


class CartItem(models.Model):

    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='+')

    class Meta:
        ordering = ('-timestamp',)
        unique_together = ('user', 'product')

    def increment_quantity(self, quantity: int = 1):
        self.quantity += quantity
        self.save()

    @property
    def total(self) -> decimal.Decimal:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f'{self.user} - {self.product}'

from django.db import models


class Heart(models.Model):

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='hearts')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='hearts')

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self) -> str:
        return f'{self.user.username} - {self.product.name}'

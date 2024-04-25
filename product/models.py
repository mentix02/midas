from django.db import models

from order.models import Order


class Product(models.Model):

    IS_HEARTED_ANNOTATION = 'is_hearted'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(null=True, blank=True, default=None)

    updated_at = models.DateTimeField(auto_now=True)

    def users_also_bought(self, n: int = 5):
        """
        A simple heuristical algorithm to fetch n products that
        were ordered by users ALONG with this product. No ML here.

        I'm a real genius, I know.
        """
        # first get all orders that contain this product
        orders = Order.objects.filter(items__product=self)
        # then get all products that were ordered along with this product
        products = Product.objects.filter(order_items__order__in=orders)
        # exclude this product from the list
        products = products.exclude(id=self.id)
        # finally, order by the number of orders
        products = products.annotate(num_orders=models.Count('order_items')).order_by('-num_orders')

        return products[:n]

    def __str__(self) -> str:
        return self.name

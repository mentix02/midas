from typing import Union

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from heart.models import Heart
from product.models import Product
from order.models import Order, OrderItem


class User(AbstractUser):

    # AbstractUser allows multiple users with the same email
    email = models.EmailField(_('email address'), unique=True)

    def toggle_product_heart(self, product_or_product_id: Union[Product, int]) -> bool:
        """
        Marks a product as hearted or unhearted by the user.
        Return True if heart is added, False if heart is removed.
        """

        if isinstance(product_or_product_id, int):
            product_id = product_or_product_id
        elif isinstance(product_or_product_id, Product):
            product_id = product_or_product_id.id
        else:
            raise ValueError('Invalid value provided for product')

        heart, created = Heart.objects.get_or_create(user=self, product_id=product_id)

        if not created:
            heart.delete()
            return False

        return True

    def checkout(self) -> Order:
        """
        Converts a user's cart into an order.
        Also deletes the cart items.
        """

        cart_items = self.cart.all()

        if cart_items.count() == 0:
            raise ValueError('Cart is empty')

        order = Order.objects.create(user=self)

        for cart_item in cart_items:
            OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
            cart_item.delete()

        return order

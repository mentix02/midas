import random

from django.core.management.base import BaseCommand, CommandParser

from user.models import User
from product.models import Product
from order.models import Order, OrderItem


class Command(BaseCommand):

    help = 'Generate fake orders'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('-n', '--number', type=int, default=100, help='Number of orders to generate (default: 100)')

    def handle(self, *args, **options):
        users = User.objects.all()
        products = Product.objects.all()

        for _ in range(options['number']):
            user = random.choice(users)
            order = Order.objects.create(user=user)

            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                quantity = random.randint(1, 6)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            self.stdout.write(self.style.SUCCESS(f'Order #{order.pk} created for {user}'))

import random

from django.core.management.base import BaseCommand, CommandParser

from user.models import User
from heart.models import Heart
from product.models import Product


class Command(BaseCommand):

    help = 'Generate fake hearts by users on products'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('-n', '--number', type=int, default=25, help='Number of products to heart')

    def handle(self, *args, **options):
        count = 0
        users = User.objects.all()
        products = Product.objects.all()

        for _ in range(options['number']):
            user = random.choice(users)
            product = random.choice(products)

            if not Heart.objects.filter(user=user, product=product).exists():
                count += 1
                Heart.objects.create(user=user, product=product)

        self.stdout.write(self.style.SUCCESS(f'Generated {count} hearts'))

import json
import decimal
import argparse

from django.core.management.base import BaseCommand

from product.models import Product


class Command(BaseCommand):
    help = 'Loads products from a JSON file into the db'

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument('products_file', type=argparse.FileType('r'), help='File to load products from')

    @staticmethod
    def transform_products(products: list[dict]) -> list[Product]:
        """
        Converts a list of dictionaries into a list of Product instances
        """
        return [
            Product(
                **{
                    'name': product['title'],
                    'image': product['image'],
                    'description': product['description'],
                    'price': decimal.Decimal(product['price']),
                }
            )
            for product in products
        ]

    def handle(self, **options):

        products = json.load(options['products_file'])
        Product.objects.bulk_create(self.transform_products(products))

        self.stdout.write(self.style.SUCCESS(f'{len(products)} products loaded successfully'))

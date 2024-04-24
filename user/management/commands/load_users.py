import json
import argparse

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from user.models import User


class Command(BaseCommand):
    help = 'Loads users from a JSON file into the db'

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument('users_file', type=argparse.FileType('r'), help='File to load users from')

    @staticmethod
    def transform_users(users: list[dict]) -> list[User]:
        """
        Converts a list of dictionaries into a list of User instances
        """
        return [
            User(
                **{
                    'email': user['email'],
                    'username': user['username'],
                    'last_name': user['name']['lastname'],
                    'first_name': user['name']['firstname'],
                    'password': make_password(user['password']),
                }
            )
            for user in users
        ]

    def handle(self, **options):

        # check for superuser and create if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@website.com', 'abcd', first_name='Mr.', last_name='Admin')

        users = json.load(options['users_file'])
        User.objects.bulk_create(self.transform_users(users))

        self.stdout.write(self.style.SUCCESS(f'{len(users)} users loaded successfully'))

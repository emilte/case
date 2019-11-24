# imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import management

# End: imports -----------------------------------------------------------------


class Command(BaseCommand):

    def handle(self, *args, **options):
        management.call_command('collectstatic', '--no-input')
        management.call_command('makemigrations')
        management.call_command('migrate')
        management.call_command('runserver')

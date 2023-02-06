# images/management/commands/createsu.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username= os.getenv('username'),
                password= os.getenv('password')
            )
        print('Superuser has been created.')
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import getpass

class Command(BaseCommand):
    help = 'Create a superuser (email login) with a secure password prompt'

    def handle(self, *args, **kwargs):
        email = input("Superuser email: ")
        password = getpass.getpass("Superuser password: ")
        User = get_user_model()
        User.objects.create_superuser(email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Superuser {email} created successfully"))

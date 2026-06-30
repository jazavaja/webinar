from django.core.management import BaseCommand

from models.models import User


class Command(BaseCommand):
    help = "Create default admin user"

    def handle(self, *args, **options):
        first_name = "admin"
        last_name = "admin"
        username = "admin"
        password = "admin"
        email = "admin@admin.com"
        gender="male"
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("Admin user already exists.")
            )
            return
        User.objects.create_superuser(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Admin user created successfully.")
        )

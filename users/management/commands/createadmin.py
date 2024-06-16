# your_app/management/commands/createcustomsuperuser.py

from django.core.management.base import BaseCommand, CommandError

from users.models import User


class Command(BaseCommand):
    help = 'Create a superuser with custom user_type field'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Superuser username', required=True)
        parser.add_argument('--email', type=str, help='Superuser email', required=True)
        parser.add_argument('--password', type=str, help='Superuser password', required=True)
        parser.add_argument('--user_type', type=int, help='Custom user type', required=True)
        parser.add_argument('--first_name', type=str, help='First name', required=True)
        parser.add_argument('--last_name', type=str, help='Last name', required=True)

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        user_type = options['user_type']
        first_name = options['first_name']
        last_name = options['last_name']

        try:
            # Create superuser
            user = User.objects.create_superuser(username=username, email=email, password=password,
                                                 user_type=user_type, first_name=first_name, last_name=last_name)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        except Exception as e:
            raise CommandError(f'Failed to create superuser: {str(e)}')

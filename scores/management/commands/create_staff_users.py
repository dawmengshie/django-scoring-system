from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.management.commands.createsuperuser import get_default_username


class Command(BaseCommand):
    help = 'Create staff users for the scoring system'

    def handle(self, *args, **options):
        staff_users = [
            {
                'username': 'sammy',
                'password': 'sammy123',
                'first_name': 'Sammy',
                'last_name': 'User'
            },
            {
                'username': 'nicos',
                'password': 'nicos123',
                'first_name': 'Nicos',
                'last_name': 'User'
            },
            {
                'username': 'Jerome',
                'password': 'jerome123',
                'first_name': 'Jerome',
                'last_name': 'User'
            },
            {
                'username': 'Adrian',
                'password': 'adrian123',
                'first_name': 'Adrian',
                'last_name': 'User'
            },
            {
                'username': 'Rouella',
                'password': 'rouella123',
                'first_name': 'Rouella',
                'last_name': 'User'
            },
            {
                'username': 'Rheajean',
                'password': 'Rhejean123',
                'first_name': 'Rheajean',
                'last_name': 'User'
            },
            {
                'username': 'Johnpaul',
                'password': 'johnpaul123',
                'first_name': 'John Paul',
                'last_name': 'User'
            },
            {
                'username': 'Princess',
                'password': 'princess123',
                'first_name': 'Princess',
                'last_name': 'User'
            },
            {
                'username': 'Kristine',
                'password': 'kristine123',
                'first_name': 'Kristine',
                'last_name': 'User'
            },
            {
                'username': 'Charlo',
                'password': 'charlo123',
                'first_name': 'Charlo',
                'last_name': 'User'
            },
            {
                'username': 'Jowyne',
                'password': 'jowyne123',
                'first_name': 'Jowyne',
                'last_name': 'User'
            },
            {
                'username': 'Emstaff',
                'password': 'Pastora',
                'first_name': 'Em Staff',
                'last_name': 'User'
            },
            {
                'username': 'Joey',
                'password': 'joey123',
                'first_name': 'Joey',
                'last_name': 'User'
            }
        ]

        created_count = 0
        updated_count = 0

        for user_data in staff_users:
            username = user_data['username']
            password = user_data['password']
            
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                # Update existing user to be staff
                if not user.is_staff:
                    user.is_staff = True
                    user.is_superuser = True  # Make them superusers for full access
                    user.save()
                    self.stdout.write(
                        self.style.WARNING(f'Updated existing user "{username}" to staff status')
                    )
                    updated_count += 1
                else:
                    self.stdout.write(
                        self.style.WARNING(f'User "{username}" already exists and is already staff')
                    )
            else:
                # Create new user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    email=f'{username.lower()}@example.com',
                    is_staff=True,
                    is_superuser=True  # Make them superusers for full access
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Created staff user "{username}"')
                )
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSummary: Created {created_count} new staff users, '
                f'updated {updated_count} existing users to staff status.'
            )
        )
        self.stdout.write(
            self.style.SUCCESS('All users now have staff privileges and can access reset functionality.')
        )

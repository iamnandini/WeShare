# In your app's management/commands directory, create a new file, e.g., createsuperuser.py

from django.contrib.auth.management.commands import createsuperuser

class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        username = options.get('username')
        email = options.get('email')
        password = options.get('password')
        
        if email and not self.UserModel.objects.filter(email=email).exists():
            self.UserModel.objects.create_superuser(email=email, username=email, password=password)
            self.stdout.write("Superuser created successfully.")
        else:
            self.stderr.write("Error: User with this email already exists.")

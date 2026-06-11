# Generated manually

from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    # Check if admin already exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    else:
        # Update its password to admin123
        user = User.objects.get(username='admin')
        user.set_password('admin123')
        user.is_superuser = True
        user.is_staff = True
        user.save()

def remove_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    User.objects.filter(username='admin').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_databasefile'),
    ]

    operations = [
        migrations.RunPython(create_superuser, remove_superuser),
    ]

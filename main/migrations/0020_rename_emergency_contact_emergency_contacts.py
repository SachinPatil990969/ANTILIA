# Generated by Django 4.2.6 on 2023-11-06 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_emergency_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='emergency_contact',
            new_name='emergency_contacts',
        ),
    ]

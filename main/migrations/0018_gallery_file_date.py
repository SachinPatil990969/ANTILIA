# Generated by Django 4.2.6 on 2023-11-02 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='file_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-02 07:02

import authentication.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_profile_gallery_gallry_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(default='default-event.png', upload_to=authentication.helpers.custom_file_name)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catagory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

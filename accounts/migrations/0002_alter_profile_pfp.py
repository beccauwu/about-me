# Generated by Django 4.0.6 on 2022-08-15 19:50

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(blank=True, upload_to=accounts.models.upload_location),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-20 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0005_image_user_likes_remove_image_likes_image_likes_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user_likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]

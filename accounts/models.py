from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_location(instance, filename):
    return f'{instance.user.username}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to=upload_location, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    dark = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

import uuid
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    username = instance.user.username
    return 'accounts/%s/%s' % (username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to=upload_location, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    dark = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# class Theme(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     #borders
#     bc = models.CharField(max_length=7, blank=True)
#     bw = models.IntegerField(blank=True)
#     br = models.IntegerField(blank=True)
#     #general colours
#     primary = models.CharField(max_length=7, blank=True)
#     light = models.CharField(max_length=7, blank=True)
#     dark = models.CharField(max_length=7, blank=True)
#     body = models.CharField(max_length=7, blank=True)

#     def __str__(self):
#         return self.profile.user

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

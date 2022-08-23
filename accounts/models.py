import uuid
import pathlib
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from about_me.validators import validate_file_size

def upload_location(instance, filename):
    ext = pathlib.Path(filename).suffix
    filename = "{}{}".format(uuid.uuid4().hex, ext)
    return 'user_{}/{}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to=upload_location, validators=[validate_file_size], blank=True)
    bio = models.CharField(max_length=200, blank=True)
    dark = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Follower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE)
    friends_since = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

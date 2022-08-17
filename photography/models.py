import collections
import uuid
import pathlib
from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    ext = pathlib.Path(filename).suffix
    filename = "{}{}".format(uuid.uuid4().hex, ext)
    return 'user_{}/gallery/{}'.format(instance.user.id, filename)

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=200, unique=True)
    summary = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.collection

class Image(models.Model):
    title = models.CharField(max_length=200, unique=True)
    likes = models.ManyToManyField(User, default=1)
    img = models.ImageField(upload_to=upload_location)
    upload_date = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, default=1, verbose_name='Collections', on_delete=models.SET_DEFAULT)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    author = models.OneToOneField(User, default=1, on_delete=models.SET_DEFAULT)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, default=1, verbose_name='Images', on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.comment

class PhotoGallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    collection = models.ForeignKey(Collection, default=1, on_delete=models.SET_DEFAULT)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Photo Galleries"

    def __str__(self):
        return self.title

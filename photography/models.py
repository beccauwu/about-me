import collections
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PhotoGallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    collection = models.CharField(max_length=200)
    img = models.FileField(upload_to =f'pics/gallery/{collection}')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Photo Galleries"

    def __str__(self):
        return self.title

class Collection(models.Model):
    collection = models.CharField(max_length=200, unique=True)
    collection_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.collection

class Image(models.Model):
    title = models.CharField(max_length=200, unique=True)
    img = models.FileField(upload_to='pics/gallery')
    collection = models.ForeignKey(Collection, default=1, verbose_name='Collections', on_delete=models.SET_DEFAULT)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    upload_date = models.DateTimeField(auto_now_add=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    image = models.ForeignKey(Image, default=1, verbose_name='Images', on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(User, default=1, verbose_name='Users', on_delete=models.SET_DEFAULT)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

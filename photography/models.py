import collections
from django.db import models

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
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

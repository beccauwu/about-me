from django.db import models

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     summary = models.CharField(max_length=200, blank=True)

#     def __str__(self):
#         return self.name

# class SubCategory(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     summary = models.CharField(max_length=200, blank=True)
#     dropdown = models.BooleanField(default=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

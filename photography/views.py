import os
from django.shortcuts import render
from django.conf import settings
from boto.s3.connection import S3Connection
from .models import Image, Collection
from .forms import GalleryForm
import boto3

# Create your views here.
def photo_gallery(request):
    form = GalleryForm(request.POST)
    collections = Image.objects.values_list('collection', flat=True).distinct()
    if request.method == "POST":
        if form.is_valid():
            images = request.FILES.getlist('images')
            collection = form.cleaned_data['collection']
            title = form.cleaned_data['title']
            if collection not in collections:
                collection_summary = form.cleaned_data['collection_summary']
                Collection.objects.create(collection=collection, collection_summary=collection_summary)
            for image in images:
                Image.objects.create(img=image, collection=collection, title=title)
    context = {}
    for collection in collections:
        images = Image.objects.filter(collection=collection)
        context[collection] = images
    return render(request, 'photos/photos.html', context)

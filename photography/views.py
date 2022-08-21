import os
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django_addanother.views import CreatePopupMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from boto.s3.connection import S3Connection
from dal import autocomplete
from .models import Image, Collection, Comment
from .forms import PhotoUploadForm, CollectionCreateForm, CommentUploadForm
from about_me.storage_backends import staturl
import boto3

class PhotoDetail(DetailView):
    model = Image
    template_name = 'photos/photo_detail.html'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['image'] = get_object_or_404(Image, id=self.kwargs['pk'])
            context['form'] = CommentUploadForm()
            print(context)
            return super().get_context_data(**context)

# Create your views here.
def photo_gallery(request):
    context = {}
    form = PhotoUploadForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    context['form'] = form
    context['scripts'] = [staturl('photos/js/photos.js')]
    return render(request, 'photos/photos.html', context)

def gallery_upload(request):
    if request.method == "POST":
        if 'collectionName' in request.POST:
            collection = Collection(
            name=request.POST['collectionName'],
            summary=request.POST['collectionSummary'],
            user = request.user
            )
            collection.save()
            image = Image(
            img = request.FILES['img'],
            title = request.POST['title'],
            collection = Collection.objects.get(id=collection.id),
            )
            image.save()
        else:
            image = Image(
            img = request.FILES['img'],
            title = request.POST['title'],
            collection = Collection.objects.get(id=request.POST['collection'])
            )
            image.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_comment(request):
    if request.method == "POST":
        comment = Comment(
        image = Image.objects.get(id=request.POST['image_id']),
        author = request.user,
        comment = request.POST['comment']
        )
        comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


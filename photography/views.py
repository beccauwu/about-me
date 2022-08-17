import os
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django_addanother.views import CreatePopupMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from boto.s3.connection import S3Connection
from dal import autocomplete
from .models import Image, Collection, Comment
from .forms import PhotoUploadForm
import boto3

class CollectionCreate(CreatePopupMixin, CreateView):
    model = Collection
    fields = ['name', 'summary']

class CollectionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Collection.objects.none()

        qs = Collection.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class PhotoDetail(DetailView):
    model = Image
    template_name = 'photos/photo_detail.html'
    context_object_name = 'image'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Image, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['liked'] = liked
        context['comments'] = Comment.objects.filter(image=self.object)
        return context

# Create your views here.
def photo_gallery(request):
    context = {}
    form = PhotoUploadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    context['form'] = form
    context['scripts'] = ["{% static 'photos/js/photos.js' %}"]
    return render(request, 'photos/photos.html', context)

def gallery_upload(request):
    form = PhotoUploadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'photos/gallery_upload.html', {'form': form})

def PhotoLike(request, pk):
    post = get_object_or_404(Image, id=request.POST.get('title'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

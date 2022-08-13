import os
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from boto.s3.connection import S3Connection
from .models import Image, Collection, Comment
from .forms import GalleryForm
import boto3

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
    collections = Image.objects.values_list('collection', flat=True).distinct()
    context = {}
    for collection in collections:
        images = Image.objects.filter(collection=collection)
        context[collection] = images
    return render(request, 'photos/photos.html', context)

def gallery_upload(request):
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
    return render(request, 'photos/gallery_upload.html', {'form': form})

def PhotoLike(request, pk):
    post = get_object_or_404(Image, id=request.POST.get('title'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

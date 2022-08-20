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
    success_url = '/photos/'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['image'] = get_object_or_404(Image, id=self.kwargs['pk'])
            context['form'] = CommentUploadForm()
            print(context)
            return super().get_context_data(**context)

def post_comment(request):
    if request.method == "POST":
        comment = Comment(
        image = Image.objects.get(id=request.POST['image_id']),
        author = request.user,
        comment = request.POST['comment']
        )
        comment.save()
    return HttpResponseRedirect(request.path_info)

class PostComment(CreateView):
    model = Comment
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.image = self.get_object()
        instance.save()
        return HttpResponseRedirect(self.request.path_info)

class CollectionCreate(CreateView):
    model = Collection
    form_class = CollectionCreateForm
    success_url = '/photography/'
    template_name = 'collection_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CollectionCreate, self).form_valid(form)

# class PhotoDetail(DetailView):
#     model = Image
#     template_name = 'photos/photo_detail.html'
#     context_object_name = 'image'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         likes_connected = get_object_or_404(Image, id=self.kwargs['pk'])
#         liked = False
#         if likes_connected.likes.filter(id=self.request.user.id).exists():
#             liked = True
#         context['number_of_likes'] = likes_connected.number_of_likes()
#         context['liked'] = liked
#         context['comments'] = Comment.objects.filter(image=self.object)
#         return context

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
    form = PhotoUploadForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'photos/gallery_upload.html', {'form': form})


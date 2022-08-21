import os
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django_addanother.views import CreatePopupMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from boto.s3.connection import S3Connection
from dal import autocomplete
from .models import Image, Collection, Comment, Like
from .forms import PhotoUploadForm, CollectionCreateForm, CommentUploadForm
from about_me.storage_backends import staturl
from accounts.models import Follower, Profile
from django.contrib import messages
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

class FollowingView(TemplateView):
    template_name = 'photos/photos.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        print(user)
        following = Follower.objects.filter(follower=user).values('user')
        if not following:
            messages.info(self.request, 'You are not following anyone')
            context['images'] = None
            return context
        following_user = User.objects.filter(id__in=following)
        print(following, following_user)
        context['images'] = Image.objects.filter(collection__user__in=following_user)
        if not context['images']:
            messages.info(self.request, 'Person(s) you follow have no posts')
        print(context)
        return context

class PhotoSearch(ListView):
    model = Image
    template_name = 'photos/photos.html'
    context_object_name = 'images'
    def get_queryset(self):
        result = super(PhotoSearch, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
          postresult = Image.objects.filter(title__contains=query)
          result = postresult
        else:
           result = None
        return result
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        if not context["images"]:
            messages.info(self.request, 'No images found')
        print(context)
        return context

class PhotosView(TemplateView):
    template_name = 'photos/photos.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context

class CollectionView(TemplateView):
    template_name = 'photos/photos.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(collection=self.kwargs['pk'])
        context['collection'] = Collection.objects.get(id=self.kwargs['pk'])
# Create your views here.

def photo_delete(request, pk):
    image = Image.objects.get(id=pk)
    image.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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
            if 'textContent' in request.POST:
                image = Image(
                title=request.POST['title'],
                img=request.FILES['image'],
                text_content=request.POST['textContent'],
                collection=collection
                )
                image.save()
            else:
                image = Image(
                title=request.POST['title'],
                img=request.FILES['image'],
                collection=collection
                )
                image.save()
        elif 'textContent' in request.POST:
                image = Image(
                title=request.POST['title'],
                img=request.FILES['image'],
                text_content=request.POST['textContent'],
                collection=Collection.objects.get(id=request.POST['collection'])
                )
                image.save()
        else:
            image = Image(
            title=request.POST['title'],
            img=request.FILES['image'],
            collection=Collection.objects.get(id=request.POST['collection'])
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

def post_like(request, pk):
    if request.user.is_authenticated:
        like = Like(
        image = Image.objects.get(id=pk),
        user = request.user
        )
        like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

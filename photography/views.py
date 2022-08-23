from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from about_me.mixins import CustomLoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Image, Collection, Comment, Like
from .forms import CommentUploadForm
from accounts.models import Follower, Profile
from django.contrib import messages

class PhotoDetail(DetailView):
    model = Image
    template_name = 'photos/photo_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = get_object_or_404(Image, id=self.kwargs['pk'])
        context['likes'] = Like.objects.filter(image=context['image'])
        context['likes_count'] = context['likes'].count()
        context['form'] = CommentUploadForm()
        print(context)
        return super().get_context_data(**context)

class FollowingView(CustomLoginRequiredMixin, TemplateView):
    template_name = 'photos/photos.html'
    login_url = '/'
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
        return context
# Create your views here.

def photo_delete(request, pk):
    if request.user.is_authenticated:
        image = Image.objects.get(id=pk)
        image.delete()
        messages.success(request, 'Image deleted')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You must be logged in to delete an image')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def comment_delete(request, pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=pk)
        comment.delete()
        messages.success(request, 'Comment deleted')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You must be logged in to delete a comment')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def gallery_upload(request):
    if request.user.is_authenticated:
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
    else:
        messages.error(request, 'You must be logged in to upload')
        return redirect('start')

def post_comment(request, pk):
    if request.user.is_authenticated:
        comment = Comment(
        image = Image.objects.get(id=pk),
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

def post_unlike(request, pk):
    if request.user.is_authenticated:
        like = Like.objects.get(image=pk, user=request.user)
        like.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, NewUserForm, ProfileForm, UserUpdateForm
from django.views.generic.base import TemplateView
from .models import update_profile_signal, Profile, Follower
from photography.models import Image
from photography.forms import PhotoEditForm, PhotoUploadForm
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from about_me.storage_backends import staturl
from django.http import HttpResponseRedirect
import getpass
# Create your views here.

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

class UserView(DetailView):
    model = User
    template_name = 'user_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userdetail'] = get_object_or_404(User, id=self.kwargs['pk'])
        context['followers'] = Follower.objects.filter(user=context['userdetail'])
        context['follower_count'] = str(context['followers'].count())
        print(context)
        return super().get_context_data(**context)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = '/'
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['follower_count'] = str(Follower.objects.filter(user=user).count())
        context['scripts'] = [staturl("accounts/js/accounts.js")]
        context['forms'] = {'profile_form': ProfileForm(instance=user.profile), 'user_form': UserUpdateForm(instance=user)}
        print(context)
        return super().get_context_data(**context)

class DeleteImageView(DeleteView):
    model = Image
    success_url = '/user/'
    template_name = 'delete_image.html'
    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['image'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)

class EditImageView(UpdateView):
    model = Image
    form_class = PhotoEditForm
    template_name = 'edit_image.html'
    success_url = '/user/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def follow_user(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, _('You are not logged in.'))
        return redirect('start')
    user = User.objects.get(id=pk)
    follower = Follower(
        user = user,
        follower = request.user.profile
        )
    follower.save()
    return redirect('profiledetails', pk=pk)

def unfollow_user(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, _('You are not logged in.'))
        return redirect('start')
    user = User.objects.get(id=pk)
    follower = Follower.objects.get(user=user, follower=request.user.profile)
    follower.delete()
    return redirect('profiledetails', pk=pk)

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        try:
            form.is_valid()
            form.user_login()
            messages.success(request, _('You have successfully logged in!'))
            if '/user/logout/' in request.get_full_path():
                return HttpResponseRedirect('/')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            messages.error(request, '{}'.format(e))
            return redirect('start')

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            auth_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, auth_user)
            messages.success(request, _('You have successfully registered!\nyou were automatically logged in.'))
            return redirect('start')
        else:
            messages.error(request, _('Please correct the error below.'))
            return redirect('start')

def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        try:
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile has been updated!'))
            return redirect('profile')
        except Exception as e:
            messages.error(request, _(f'{e}'))
            return redirect('profile')

def logout_request(request):
    logout(request)
    messages.success(request, _('You have been logged out.'))
    return redirect('start')

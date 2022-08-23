from django.contrib.auth.models import User
from about_me.mixins import CustomLoginRequiredMixin
from .forms import LoginForm, NewUserForm, ProfileForm, UserUpdateForm
from django.views.generic.base import TemplateView
from .models import Follower
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView
from about_me.storage_backends import staturl
from django.http import HttpResponseRedirect
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

class ProfileView(CustomLoginRequiredMixin, TemplateView):
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
        if form.is_valid():
            form.user_login()
            messages.success(request, _('You have successfully logged in!'))
            if '/user/logout/' in request.get_full_path():
                return HttpResponseRedirect('/')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Wrong username or password.')
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

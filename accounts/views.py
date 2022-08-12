from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import LoginForm, NewUserForm, ProfileForm, UserUpdateForm
from django.utils.translation import gettext_lazy as _
# Create your views here.

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid() and form.user_login() is not None:
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    form = LoginForm()
    return render(request=request, template_name='login.html', context={'form':form})

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(data=request.POST, instance=request.user, created=True, request=request)
        if form.is_valid():
            user = form.save()
            users_group = Group.objects.get(name='users')
            user.refresh_from_db()
            users_group.user_set.add(user)
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'signup.html', {'form': form})

def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {'user_form': user_form, 'profile_form': profile_form})

def logout_request(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))

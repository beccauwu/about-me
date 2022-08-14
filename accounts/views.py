from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .forms import LoginForm, NewUserForm, ProfileForm, UserUpdateForm
from .models import update_profile_signal
from django.utils.translation import gettext_lazy as _
# Create your views here.

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def login_request(request):
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        form.user_login()
        return redirect('home')
    else:
        messages.error(request, 'Invalid username or password')
    # form = LoginForm()
    # return render(request=request, template_name='login.html', context={'form':form})

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            update_profile_signal(sender=User, instance=user, created=True, request=request)
            users_group = Group.objects.get(name='users')
            user.refresh_from_db()
            users_group.user_set.add(user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    # else:
    #     form = NewUserForm()
    # return render(request, 'signup.html', {'form': form})

def profile(request):
    context = {}
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST, instance=request.user, request=request)
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile, request=request)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context['forms'] = {'user_form': user_form, 'profile_form': profile_form}
    context['scripts'] = ["{% static 'accounts/js/accounts.js' %}"]
    return render(request, 'profile.html', context)

def logout_request(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))

from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import SignupForm, LoginForm
# Create your views here.

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = LoginForm()
    return render(request=request, template_name='login.html', context={'login_form':form})

def logout_request(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('fname')
            user.profile.last_name = form.cleaned_data.get('lname')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            users_group = Group.objects.get(name='users')
            users_group.user_set.add(user)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .forms import LoginForm, NewUserForm, ProfileForm, UserUpdateForm
from .models import update_profile_signal, Profile
from photography.models import Image
from photography.forms import PhotoEditForm, PhotoUploadForm
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from about_me.storage_backends import staturl
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
        user_form = NewUserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    # else:
    #     form = NewUserForm()
    # return render(request, 'signup.html', {'form': form})

def profile(request):
    context = {}
    user = request.user
    profile  = user.profile
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            update_profile_signal(sender=User, instance=user, created=False, request=request)
            messages.success(request, _('Your profile was successfully updated!'))
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    context['forms'] = {'user_form': user_form, 'profile_form': profile_form, 'upload_form': PhotoUploadForm}
    context['scripts'] = [staturl("accounts/js/accounts.js")]
    return render(request, 'profile.html', context)

def logout_request(request):
    logout(request)
    return redirect('home')


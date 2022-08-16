from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect
from accounts.forms import LoginForm, NewUserForm, ProfileForm

class LoginFormMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                form.user_login()
                if '/user/logout/' in request.get_full_path():
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm(request)
        request.login_form = form

class SignupFormMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST':
            signup_form = NewUserForm(data=request.POST)
            profile_form = ProfileForm(request.POST, request.FILES)
            if signup_form.is_valid():
                user = signup_form.save()
                user.refresh_from_db()
                profile_form.save()
                if '/user/logout/' in request.get_full_path():
                    return HttpResponseRedirect('/')
        else:
            signup_form = NewUserForm(request)
            profile_form = ProfileForm(request)
        request.signup_form = signup_form
        request.profile_form = profile_form

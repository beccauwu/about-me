from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect
from accounts.forms import LoginForm, NewUserForm

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
            form = NewUserForm(data=request.POST)
            if form.is_valid():
                form.save()
                if '/user/logout/' in request.get_full_path():
                    return HttpResponseRedirect('/')
        else:
            form = NewUserForm(request)
        request.signup_form = form
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect, redirect
from django.contrib import messages
from accounts.forms import LoginForm, NewUserForm, ProfileForm

class LoginFormMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                form.user_login()
                messages.success(request, 'You have successfully logged in!')
                if '/user/logout/' in request.get_full_path():
                    return redirect('start')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('start')
        else:
            form = LoginForm(request)
        request.login_form = form


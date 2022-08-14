from django.utils.deprecation import MiddlewareMixin
from accounts.forms import LoginForm

class LoginFormMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                form.user_login()
                if '/user/logout/' in request.get_full_path():
                    from django.shortcuts import HttpResponseRedirect
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm(request)
        request.login_form = form
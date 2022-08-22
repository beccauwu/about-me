from accounts.forms import LoginForm, NewUserForm
from django.contrib.auth.models import User
        

def add_account_forms(request):
    return {
        'signup_form': NewUserForm(),
        'login_form': LoginForm(),
        'users': User.objects.all()
        }
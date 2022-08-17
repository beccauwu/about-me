from accounts.forms import LoginForm, NewUserForm
from django.contrib.auth.models import User
        

def add_account_forms(request):
    return {
        'signup_form': NewUserForm(),
        'users': User.objects.all()
        }
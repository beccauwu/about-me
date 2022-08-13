from accounts.forms import LoginForm, NewUserForm

def add_account_forms(request):
    return {
        'login_form': LoginForm(),
        'signup_form': NewUserForm()
        }
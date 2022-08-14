from accounts.forms import LoginForm, NewUserForm
        

def add_account_forms(request):
    return {
        'signup_form': NewUserForm()
        }
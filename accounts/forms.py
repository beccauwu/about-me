from django.forms import CharField, TextInput, EmailField, Form, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

class SignupForm(UserCreationForm):
    fname = CharField(max_length = 50, required=True, widget=TextInput(attrs={'class': "form-control giBold nameInput", 'id': 'fnameInput', 'placeholder': 'Nathaneal'}))
    lname = CharField(max_length = 50, required=True, widget=TextInput(attrs={'class': "form-control giBold nameInput", 'id': 'lnameInput', 'placeholder': 'Down'}))
    username = CharField(max_length = 50, required=True, widget=TextInput(attrs={'class': "form-control giBold", 'id': 'usernameInput', 'placeholder': 'Username'}))
    email = EmailField(max_length = 150, required=True, widget=EmailInput(attrs={'class': "form-control giBold", 'id': 'emailInput', 'placeholder': 'name@example.com'}))
    password1 = CharField(max_length = 50, required=True, widget=PasswordInput(attrs={'class': "form-control giBold", 'id': 'password1Input', 'placeholder': 'Password'}))
    password2 = CharField(max_length = 50, required=True, widget=PasswordInput(attrs={'class': "form-control giBold", 'id': 'password2Input', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'fname', 'lname', 'email', 'password1', 'password2')

class LoginForm(Form):
    username = CharField(max_length = 50, required=True, widget=TextInput(attrs={'class': "form-control giBold", 'id': 'usernameInput', 'placeholder': 'Username'}))
    password = CharField(max_length = 50, required=True, widget=PasswordInput(attrs={'class': "form-control giBold", 'id': 'passwordInput', 'placeholder': 'Password'}))
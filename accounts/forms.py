from django.forms import CharField, TextInput, EmailField, Form, EmailInput, PasswordInput, ImageField
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Profile

# Create your forms here.

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form-control giBold", 'id': 'usernameInput', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': "form-control giBold", 'id': 'emailInput', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': "form-control giBold", 'id': 'password1Input', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': "form-control giBold", 'id': 'password2Input', 'placeholder': 'Confirm Password'})

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form-control giBold", 'id': 'usernameChangeInput', 'placeholder': 'Change username'})
        self.fields['email'].widget.attrs.update({'class': "form-control giBold", 'id': 'emailChangeInput', 'placeholder': 'Change email'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pfp', 'bio')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pfp'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Profile Picture'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Bio'})

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form-control giBold", 'id': 'usernameInput', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': "form-control giBold", 'id': 'passwordInput', 'placeholder': 'Password'})
    def user_login(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            return user
        else:
            return None

from logging import setLogRecordFactory
from django.forms import CharField, TextInput, EmailField, Form, EmailInput, PasswordInput, ImageField
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext, gettext_lazy as _
from about_me.widgets import CustomCropWidget
from .models import Profile

# Create your forms here.

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)
        self.fields['username'].widget.attrs.update({'class': "form-control giBold mb-2 text-center bg-internal-light-dark", 'id': 'signupUsernameInput', 'placeholder': 'greatestusername'})
        self.fields['email'].widget.attrs.update({'class': "form-control giBold mb-2 text-center bg-internal-light-dark", 'id': 'signupEmailInput', 'placeholder': 'mail@example.com'})
        self.fields['password1'].widget.attrs.update({'class': "form-control giBold mb-2 text-center bg-internal-light-dark", 'id': 'password1Input', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': "form-control giBold mb-2 text-center bg-internal-light-dark", 'id': 'password2Input', 'placeholder': 'Confirm Password'})
    def save(self, commit=True, **kwargs):
        from .models import update_profile_signal
        user = super().save(commit=commit)
        if commit:
            auth_user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password1'])
            login(self.request, auth_user)

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
        widgets = {
            'pfp': CustomCropWidget(
                width=300,
                height=300,
                preview_height=100,
                preview_width=100,
                format='png',
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pfp'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Profile Picture', 'id': 'pfpInput'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Bio', 'id': 'bioInput'})

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "form-control giBold text-center", 'id': 'loginUsernameInput'})
        self.fields['password'].widget.attrs.update({'class': "form-control giBold text-center", 'id': 'loginPasswordInput'})
        
    def user_login(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is not None:
            login(self.request, user)

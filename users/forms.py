from users.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import LoginForm, SignupForm


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [('first_name'), ('last_name')]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [('image'), ('age'), ('weight'), ('hight')]

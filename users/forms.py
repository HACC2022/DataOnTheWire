from django import forms
from django.contrib.auth import get_user_model

from users.models import User
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'department', 'password1', 'password2']

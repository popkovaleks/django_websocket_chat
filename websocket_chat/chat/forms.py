from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ChatUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = ChatUser
        fields = ('username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = ChatUser
        fields = ('username',)
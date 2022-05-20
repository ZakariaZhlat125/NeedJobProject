
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm (UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','email','age',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=User
       # fiel=UserChangeForm.Meta.fields
        fields=('username','email','age',)
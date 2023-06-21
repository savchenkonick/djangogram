from django import forms
from .models import DgUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = DgUser
        fields = ('username', 'email', 'password', 'first_name',
                  'last_name', 'bio_info', 'profile_pic')
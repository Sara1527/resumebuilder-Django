from django import forms
from . models import Resume
from django.contrib.auth.models import User

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields= "__all__"

class signinform(forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'password')

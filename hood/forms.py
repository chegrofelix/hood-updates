from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hood, Business, Profile, Post, Social_Ammenities

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['hood', 'user']
        

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email_confirmed']


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['hood', 'user']

class NewSocialForm(forms.ModelForm):
    class Meta:
        model = Social_Ammenities
        exclude = ['hood']


class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('hoodName', 'hoodLocation', 'occupantsCount', 'admin')
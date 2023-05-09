from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'price')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,required=True,help_text='Required. Enter a valid email.adress')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
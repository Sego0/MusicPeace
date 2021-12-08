from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from Peace.models import Post
from .models import Post

class UserRegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control w-100", "id":"contentsBox","rows":"3",
    "placeholder":"Coloca tu post aqui, indicar titulo, instumento y autor (seguir plantilla del primer post)"}))

    class Meta:
        model = Post
        fields = ["content"]
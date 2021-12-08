from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import Profile, Post
from .forms import UserRegisterFrom, PostForm
from  django.contrib.auth.models import User

def ini(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("Inicio")
    else:
        form = PostForm()    
    context = {"posts":posts, "form": form}
    return render(request, "prin.html", context)

def sob(request):
    return render(request, "sobre.html")

def crea(request):
    return render(request, "crea.html")
    
def usu(request):
    return render(request, "usu.html") 

def log(request):
    return render(request, "log.html") 

def reg(request):    
    if request.method == "POST":
        form = UserRegisterFrom (request.POST)
        if form.is_valid():
            form.save()
            return redirect("Inicio")
    else:
        form= UserRegisterFrom()
    context = {"form" : form}    
    return render(request, "reg.html", context)               

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("Inicio")

def profile(request,username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {"user":user, "posts":posts}
    return render(request, "profile.html",context)
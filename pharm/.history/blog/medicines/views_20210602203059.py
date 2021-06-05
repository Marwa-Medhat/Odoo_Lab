from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Medicine

def index(request):
    posts = Medicine.objects.all()# Post name of module
    return render(request,"medicines/index.html",{
    "posts":posts
    })
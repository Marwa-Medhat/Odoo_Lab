from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
def index(request):
    return HttpResponse("hello")
# posts = Post.objects.all()# Post name of module
# return render(request,"posts/index.html",{
# "posts":posts
# })
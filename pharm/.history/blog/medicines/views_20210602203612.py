from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Medicine
import requests

# def index(request):
#     posts = Medicine.objects.all()# Post name of module

#     ##yb3t request llodoo b url http://192.168.1.13:8069/iti_os41/objects/ ygeb mno al data 
#     return render(request,"medicines/index.html",{
#     "posts":posts
#     })



def index(request):
    response = requests.get('http://192.168.1.13:8069/iti_os41/objects/ ')
    geodata = response
    return HttpResponse(geodata)

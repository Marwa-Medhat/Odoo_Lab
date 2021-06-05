from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Medicine
import requests

import urllib,json

# def index(request):
#     posts = Medicine.objects.all()# Post name of module

#     ##yb3t request llodoo b url http://192.168.1.13:8069/iti_os41/objects/ ygeb mno al data 
#     return render(request,"medicines/index.html",{
#     "posts":posts
#     })



def index(request):
    # r = requests.get('http://192.168.1.13:8069/iti_os41/objects/')
    # print (r) 
    # # r = requests.get('url')
    # # print (r.json())   
    # # geodata = response
    # return HttpResponse('hi')
    # try:
    #     data=json.loads(request.raw_post_data)
    #     url=data['url']
    #     print  (url)
    # except:
    #     print ('nope')
    # return HttpResponse('hi')  
    url = "put url here"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print (data)  

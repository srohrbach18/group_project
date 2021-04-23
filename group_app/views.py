from django.shortcuts import render
from django.urls import path
from . models import *

def login(request):
    return render(request,'log_and_reg.html')

def index(request):
    return render (request, "index.html")

def contact (request):
    return render(request,'contact.html')

def profile(request):
    
    return render(request,'profile.html')

# def order(request):
    
#     return render(request,'order.html')


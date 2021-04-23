from django.shortcuts import render
from django.urls import path
from . models import *

def index(request):

    return render(request,'index.html')

def contact (request):
    return render(request,'contact.html')


def profile(request):
    
    return render(request,'profile.html')

def order(request):
    
    return render(request,'order.html')

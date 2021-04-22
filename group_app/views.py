from django.shortcuts import render
from django.urls import path
from . models import *

def index(request):

    return render(request,'index.html')

    


def profile(request):
    
    return render(request,'profile.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def login(request):
    return render(request,'log_and_reg.html')

def contact (request):
    return render(request,'contact.html')

def profile(request):
    
    return render(request,'profile.html')

def index(request):
    return render(request, 'order.html')

def order(request):
    return render(request, 'order.html')

def checkout(request):
    context ={
    }
    return render(request, 'store/checkout.html', context)

def purchase(request):
    return redirect('/')

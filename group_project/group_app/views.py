from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def login(request):
    return render(request,'log_and_reg.html')

def contact (request):
    return render(request,'contact.html')

def edit_user (request):
    # ("??need user id to add to path??")

    # if request.method=='POST':
        # if "edit_btn":
        #     user=user.objects.get(id=user_id)
        #     user.first_name=request.POST['first_name'].capitalize()
        #     user.last_name=request.POST['last_name'].capitalize()
        #     user.email=request.POST['email']
        #     user.phone_number=request.POST['phone_number']    
        #     user.save()
    return redirect(profile)

def edit_card (request):

    return redirect(profile)

def profile(request):
    # (??"need to add id to path"??)

    return render(request,'profile.html')

def index(request):
    return render (request, "index.html")


def welcome(request):
    return render (request, "welcome.html")

def order(request):
    return render(request, 'order.html')

def checkout(request):
    context ={
    }
    return render(request, 'store/checkout.html', context)

def purchase(request):
    return redirect('/')


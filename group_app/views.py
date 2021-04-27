from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import *
import bcrypt


def login(request):
    return render(request,'log_and_reg.html')

def contact (request):
    return render(request,'contact.html')

def edit_user (request):
    # (" ??need user id to add to path??")

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

def register(request):
    errors = User.objects.register_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/')


# def login(request):
#     errors = User.objects.login_validator(request.POST)

#     if len(errors):
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/')
#     else:
#         user = User.objects.get(email=request.POST['login_email'])
#         request.session['user_id'] = user.id
#         request.session['greeting'] = user.first_name
#         return redirect('/')

def order(request):
    return render(request, 'order.html')

def checkout(request):
    context ={
    }
    return render(request, 'store/checkout.html', context)

def purchase(request):
    return redirect('/')


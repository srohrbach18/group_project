from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from . models import *
import bcrypt


def contact (request):
    return render(request,'contact.html')

def logout(request):
    request.session.flush()
    return redirect(login)

def edit_user (request):
    errors = User.objects.user_validator(request.POST)
    
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/profile')
    else:
        user_id = request.session['user_id']
        user=User.objects.filter(id = user_id)
        if user:
            user = user[0]
        if request.method=='POST':
                user.first_name=request.POST['first_name'].capitalize()
                user.last_name=request.POST['last_name'].capitalize()
                user.email=request.POST['email'] 
                user.save()
        return redirect(profile)


def delete_food(request, item_id):
    item=Item.objects.filter(id=item_id)
    if item:
        d_item=item[0]
        d_item.delete()
    return redirect(add_food)


def admin(request):
    user_id = request.session['user_id']
    user=User.objects.filter(id = user_id)
    if user:
        user = user[0]
        if request.POST['_admin']=='true':
            user.is_admin = True
            active=user.is_admin = True
            user.save()
        elif request.POST['_admin']=='false':
            user.is_admin = False
            active=user.is_admin = False
            user.save()
            print(user.is_admin)
        return redirect(profile)


def profile(request):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        user_id = request.session['user_id']
        user=User.objects.filter(id = user_id)
        items=Item.objects.all()
        if user:
            user = user[0]
            first_name=user.first_name.capitalize()
            last_name=user.last_name.capitalize()
            email=user.email
        context={
            'items':items,
            'email':email,
            'user':user,
            'first_name':first_name,
            'last_name':last_name
        }

        return render(request, 'profile.html',context)

def index(request):
    return render (request, "index.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
    
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['user_id'] = user.id
        return redirect('/')
    
def login(request):
            return render (request,'log_and_reg.html')

def handle_login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/login')
    else:
        user = User.objects.filter(email=request.POST['login_email'])
        user=user[0]
        request.session['user_id'] = user.id
        return redirect('/')


def menu (request):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        items=Item.objects.all()
        context = {
            'items': items,
            'this_user': User.objects.get(id=request.session['user_id']),
        }
    return render(request, "menu.html", context) 

def handle_add_food(request):
    errors = Item.objects.item_validator(request.POST)
    
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(add_food)

    else:
        item=Item.objects.all()
        user_id = request.session['user_id']
        user=User.objects.filter(id=user_id)
        if user:
            user=user[0]
        if request.method=='POST':
            item=Item.objects.create(
                course=request.POST['course'],
                name=request.POST['name'].capitalize(),
                desc=request.POST['desc'].capitalize(),
                price=request.POST['price'] ,
                # made_by=user
                )
            item.save()
        return redirect(add_food)
    
def add_food(request):
    items=Item.objects.all()
    
    context={
        
        "items":items,
    }

    return render(request,'add_food.html',context)

def edit_item(request,item_id):
    item=Item.objects.filter(id=item_id)
    if item:
        
        item=item[0]

    context={
        
        "item":item
    }
    
    return render(request,'edit_item.html',context) 

def handle_edit_item(request,item_id):
    errors = Item.objects.item_validator(request.POST)
    
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit_item/{item_id}')
    
    else:
        request.method == 'POST'
        item=Item.objects.filter(id=item_id)
        if item:
            item=item[0]
            item.name = request.POST['name'].capitalize()
            item.desc = request.POST['desc'].capitalize()
            item.price = request.POST['price']
            item.course = request.POST['course']
            item.save()

    return redirect(add_food)



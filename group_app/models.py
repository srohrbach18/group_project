from django.db import models

class Item(models.Model):
    desc = models.TextField(max_length=100)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Menu (models.Model):
    item = models.ManyToManyField(Item)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pay (models.Model):
    # user = models.ForeignKey(User,related_name='pay' ,on_delete=models.CASCADE)
    # card_num = models.ForeignKey(User,on_delete=models.Cascade)
    card = models.IntegerField(max_length=16)
    exp = models.IntegerField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Billing (models.Model):
    address = models.TextField(max_length=100)
    phone_number = models.IntegerField(max_length=10)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


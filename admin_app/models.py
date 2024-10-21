from django.db import models
from watch_app.models import *


# Create your models here.


class Register(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField(default=0)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)


class Login(models.Model):
    uname = models.CharField(max_length=30)
    uemail = models.EmailField()

class Category(models.Model):
    category = models.CharField(max_length=30)
    category_image = models.ImageField(upload_to="categories")


class Item(models.Model):
    brand = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_model = models.CharField(max_length=20)
    price = models.IntegerField()
    item_image = models.ImageField(upload_to="items")


class Cart_item(models.Model):
    user_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    brand = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
    status = models.IntegerField(default=0)


class Checkout(models.Model):
   uname = models.ForeignKey(Register,on_delete=models.CASCADE,null='false')
   cart_product = models.ForeignKey(Cart_item,on_delete=models.CASCADE,null='false')
   address = models.CharField(max_length=50)
   city = models.CharField(max_length=50)
   state = models.CharField(max_length=50)
   pincode = models.IntegerField()
   tarea = models.CharField(max_length=500,default='tarea_area')


class Contact(models.Model):
    cname = models.CharField(max_length=20)
    cemail = models.EmailField()
    tarea = models.CharField(max_length=200)

    


    


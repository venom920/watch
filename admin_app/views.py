from django.shortcuts import render,redirect
from .models import *
from watch_app import *
from watch_app.models import *

# Create your views here.

      #CATEGORY


def category(request):
    
    if request.method == "POST":
        category = request.POST['category']
        category_image = request.FILES['category_image']

        Category.objects.create(
            category = category,
            category_image = category_image
        )
    return render(request,"add_category.html")

def view_categories(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, "all_categories.html" ,context)



def update_category(request,id ):
    if request.method == "POST":
        category = request.POST['category']
        category_image = request.FILES['category_image']

        Category.objects.filter(id=id).update(
             category = category,
            category_image = category_image
        )
        return redirect('view_categories')
    return render(request, "category.html")


def delete_category(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('view_categories')



     #ITEMS

def items(request):
    user_name = request.session.get('u_name')
    brands = Category.objects.all()
    context = {
        'brands':brands,
        'user_name':user_name
    }
    if request.method == "POST":
        brand_id = request.POST['brand']
        item_model = request.POST['model']
        price = request.POST['price']
        item_image = request.FILES['item_image']

        Item.objects.create(
            brand = Category.objects.get(id=brand_id),
            item_model = item_model,    
            price = price,
            item_image = item_image
        )
    return render(request,'add_item.html', context)

def view_items(request):
    items = Item.objects.all()
    context = {
        'item':items
    }
    return render(request, "all_item.html", context)
           

     
def main(request):
    user_name = request.session.get('u_name')
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'user_name':user_name
    }
    return render(request,"index.html",context)


def products(request):
    categories = Category.objects.all()
    brands = Item.objects.all()
    context = {
        'brands':brands,
        'categories':categories
    }
    return render(request,"all_products.html",context)


def filter_watch(request,id):
    categories = Category.objects.all()
    fwatch = Item.objects.filter(brand=id)
    context ={
        'fwatch' : fwatch,
        'categories' : categories
    }
    return render(request,"all_category_items.html",context)
    

    
def single_product(request,id):
    categories = Category.objects.all()
    single = Item.objects.filter(id=id)
    context ={
      'categories' : categories,
      'single':single  
    }
    return render(request,"single_item_details.html",context)



    #CART


def add_cart(request, product_id):
    product_price = Item.objects.get(id=product_id).price
    userid = request.session.get('uid')
    Cart_item.objects.create(
        user_id = Register.objects.get(id=userid),
        brand = Item.objects.get(id=product_id),
        quantity = 1,
        price = product_price,
    )
    return redirect("view_cart")



def view_cart(request):
    categories = Category.objects.all()
    userid = request.session.get('uid')
    cart_details = Cart_item.objects.filter(user_id=userid,status=0)
    context = {
        'categories' : categories,
        'cart_details' : cart_details
    }
    return render(request,"cart.html",context)


def delete_cart(request,id):
    Cart_item.objects.filter(id=id).delete()
    return redirect('view_cart')

def confirm_checkout(request):
    
    cdata = Checkout.objects.all()
    context = {
        'cdata' : cdata,   
    }
    return render(request,"all-checkouts.html",context)



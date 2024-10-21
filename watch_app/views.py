from django.shortcuts import render,redirect
from .models import *
from admin_app.models import *
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        pincode = request.POST['pincode']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        

        if password == cpassword:
            if not Register.objects.filter(email = email).exists():
    
                Register.objects.create(
                    fname = fname,
                    lname = lname,
                    address = address,
                    city = city,
                    country = country,
                    pincode = pincode,
                    number = number,
                    email = email,
                    password = password,
                    
                )
                return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('register')
            
        
    return render(request,"registration.html")


def registration_details(request):
    data = Register.objects.all()
    context = {
        'data': data
    }
    return render(request, "all_registrations.html", context) 


def login(request):
    if request.method == 'POST':
        uemail = request.POST['uemail']
        password = request.POST['password']

        if Register.objects.filter(email=uemail, password=password).exists():
            data = Register.objects.filter(email=uemail, password=password).values('id', 'fname').first()
            request.session['uid'] = data['id']
            request.session['u_name'] = data['fname']
            request.session['u_email'] = uemail
            return redirect('main')
        
        elif uemail == 'watchadmin123@gamil.com' and password == 'watchadmin':
            return redirect('category')
        

        else:
            return redirect('login')
        
    return render(request,"user_login.html")
        

def view_login(request):
    data = Login.objects.all()
    context = {
        'data': data
    }
    return render(request, "all_login.html", context) 




def checkout(request):
    if request.method == "POST":
        userid = request.session.get('uid')
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        tarea = request.POST['tarea']

        buy = Cart_item.objects.filter(user_id=userid,status=0)
        for i in buy :
            Checkout.objects.create(
            uname = Register.objects.get(id=userid),
            cart_product = Cart_item.objects.get(id = i.id),
            address = address,
            city = city,
            state = state,
            pincode = pincode,
            tarea = tarea
            )
      
            Cart_item.objects.filter(user_id=userid).update(status=1)
            send_mail(
        'Welcome to Horology Store',
        'Congragulations ,successfully registerd in Horology Store',
        'souravas009@gmailcom',
        ['souravas009@gmail.com'],
        fail_silently=False,
        )

        return redirect('success')
    

        
    return render(request,"checkout.html")


def order(request):
    categories = Category.objects.all()
    userid = request.session.get('uid')
    data = Checkout.objects.filter(uname=userid)
    
    context = {
        'categories' : categories,
        'data' : data
    }
    
   
    return render(request,"my_order.html",context)


def success(request):
    return render(request,'checkout_success.html')


def contact(request):
    categories = Category.objects.all()
    if request.method == "POST":
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        tarea = request.POST['tarea']

        data=Contact(
            cname = cname,
            cemail = cemail,
            tarea = tarea
        )
        data.save()
    context = {
        'categories' : categories
    }
    return render(request,'contact_us.html',context)


def view_contact(request):
    
    data = Contact.objects.all()
    
    context = {
        
        'data' : data,
        
    }
    return render(request,"view_contact.html",context) 
 
def user_account(request):
    userid = request.session.get('uid')
    data = Register.objects.filter(id=userid)
    context = {
        'data': data
    }
    return render(request, "userinfo.html", context) 


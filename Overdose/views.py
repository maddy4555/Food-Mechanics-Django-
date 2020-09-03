from django.shortcuts import render,redirect
from .models import Item,Slot,Cart,Order,Contact,Phone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from UnderBelly.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.db.models import Sum,F
from django.core import serializers
from django.utils import timezone
import json
# Create your views here.
def home(request):
    '''if request.method=='POST':
        if 'log' in request.POST:
            username=request.POST['username']
            password=request.POST['password']
        
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request,"Successfully Logged in.")
                return redirect("/Overdose/")
            else:
                messages.error(request,"Invalid Credentials")
                return redirect("/Overdose/")
        elif 'res' in request.POST:
            username=request.POST['username']
            fname=request.POST['fname']
            lname=request.POST['lname']    
            email=request.POST['email']
            phone=request.POST['phone']
            password=request.POST['password']
            check=auth.authenticate(username=username)
            if check is None:
                return HttpResponse("User already exist")
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
                user.save()
                subject = 'Welcome at Overdose'
                message = 'We wish you to enjoy our service and hospitality.'
                recepient = email
                send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)  
                return redirect("/Overdose/")
        else:
            pass '''   
    return render(request,'home.html')

  

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']    
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        check=auth.authenticate(username=username)
        if check is None:
            return HttpResponse("User already exist")
        else:
            user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
            user.save()
            new=Phone(phone=phone,author=user)
            new.save()
            '''subject = 'Welcome at Overdose'
            message = 'We wish you to enjoy our service and hospitality.'
            recepient = email
            send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)'''  
            return redirect("/Overdose/")
    else:
        return HttpResponse("404-Not Found")

def login(request):
    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully Logged in.")
            return redirect("/Overdose/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/Overdose/")
    else:
        pass
def logout(request):
    auth.logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect("/Overdose")            

#@login_required(login_url='/login')
def southindian(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        #t=[]
        #s=[]
        s=Item.objects.filter(category="southindian")
        d=len(s)
        #for i in range(1,len(s)):
         #   t.append(i)
     #quantity=$('#qty option:selected').val()
        params={'items':s}
    
 
    
        return render(request,'southindian.html',params)
    
def italian(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        d=Item.objects.filter(category="italian",subcategory="Veg.")
        f=Item.objects.filter(category="italian",subcategory="Non-Veg.")
        params={'vegitems':d,'nonvegitems':f}
        return render(request,'italian.html',params)    

def chinese(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        s=Item.objects.filter(category="chinese",subcategory="Veg.")
        g=Item.objects.filter(category="chinese",subcategory="Non-Veg.")
        params={'vegitems':s,'nonvegitems':g}
        return render(request,'chinese.html',params)

def indian(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        s=Item.objects.filter(category="indian",subcategory="Veg.")
        g=Item.objects.filter(category="indian",subcategory="Non-Veg.")
        params={'vegitems':s,'nonvegitems':g}
        return render(request,'indian.html',params)

def savouries(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:

        s=Item.objects.filter(category="savouries",subcategory="Veg.")
    
        g=Item.objects.filter(category="savouries",subcategory="Non-Veg.")
        params={'vegitems':s,'nonvegitems':g}

        return render(request,'savouries.html',params)

def breads(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:

        s=Item.objects.filter(category="breads")
        params={'items':s}
        return render(request,'breads.html',params)

def drinks(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        s=Item.objects.filter(category="drinks")
        params={'items':s}
        return render(request,'drinks.html',params)

def icecream(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        s=Item.objects.filter(category="icecream")
        params={'items':s}
        return render(request,'icecream.html',params)

def bakery(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        s=Item.objects.filter(category="bakery")
        params={'items':s}
        return render(request,'bakery.html',params) 

def about(request):
    return render(request,'about.html')

def feedback(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:

        return render(request,'feedback.html')

def contact(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        hi=request.user    
        if request.method=="POST":
            a=User.objects.get(username=hi)
            d=a.first_name
            c=a.last_name
            f=a.email
            j=str(str(d)+str(c))
            phone=Phone.objects.get(author=hi)
            l=phone.phone
            print(j)
            print(f)
            order = request.POST['order']
            desc = request.POST['desc']
            check=Order.objects.filter(order_id=order)
            check2=Order.objects.get(order_id=order)
            k=check2.order_id
            if len(check)==0:
                thank=True
                valid={'thank':thank}
                return render(request, 'contact.html',valid)
            elif len(check2)==0:
                thank=True
                valid={'thank':thank}
                return render(request, 'contact.html',valid)    
            else:
                contact = Contact(name=j, email=f, phone=l, order_id=k,desc=desc)
                contact.save()
                done=True
                valid={'done':done}
                return render(request, 'contact.html',valid)
        return render(request, 'contact.html')   



def orders(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        hi=request.user
        a=Order.objects.filter(OrderBy=hi,cancel="None")
        if len(a)==0:
            thank=True
            hello={'thank':thank}
            return render(request,'orders.html',hello)
        else:    
            params={'items':a}
            return render(request,'orders.html',params)


def reservation(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:    
        return render(request,'reservation.html')


def thank(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        return render(request,'thankyou.html')
def checkout(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        hi=request.user
        s=Cart.objects.filter(author=hi)
        k=Cart.objects.filter(author=hi).aggregate(total=Sum(F('price')*F('quantity')))
        x=k['total']
        #sj=serializers.serialize('json',s)
        tr=Cart.objects.filter(author=hi).values('item','quantity')
        mylist=[]
        for i in tr:
            p=i['item']
            e=i['quantity']
            tr1=Item.objects.get(id=p)
            w=tr1.item_name
            q=tr1.price
        
            mylist.append({'item':w,'price':q,'quantity':e})
        print(mylist)    
        
        a=Slot.objects.filter(choice="hostel_delivery",available=True)
        b=Slot.objects.filter(choice="meal_at_overdose",available=True)
        params={'hostel_time':a,'overdose_time':b,'items':s,'price':x}

        if request.method=='POST':
            #print(slot)
            #items=request.POST[]
            delivery=request.POST['hello']
            slottime=request.POST['slot']
            print(slottime)
            std=Slot.objects.get(id=slottime)
            seat=std.seats
            print(seat)
            print(std)
            a=timezone.now()
        
            if x==None:
                return redirect('/Overdose/Cartie/')
            else:
                done=Order(items=mylist,amount=x,slottime=std,placed=a,delivery=delivery,OrderBy=hi)
                done.save()
                removeall=Cart.objects.filter(author=hi)
                removeall.delete()
                seat=seat-1
                Slot.objects.filter(id=slottime).update(seats=seat)
                if seat==0:
                    Slot.objects.filter(id=slottime).update(available=False)
                return redirect('/Overdose/thankyou')
        return render(request,'checkout.html',params)   

def cart(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        global wat
        wat=request.user
        if request.method=='GET':
            post_id = int(request.GET['post_id'])
            quantity1=int(request.GET['quantity1'])
            print(quantity1)
            likedpost = Item.objects.get(id = post_id )
        
            c=likedpost.item_name
            d=likedpost.price
            
            m = Cart( item=likedpost,price=d,quantity=quantity1,author=wat)
            m.save()
            '''w=Tprice.objects.get(author=wat)
            h=w.tprice
            
            h=h+d
            
            Tprice.objects.filter(author=wat).update(tprice=h)'''
            

            #m.user.add(request.user)
            return HttpResponse('success')
            '''elif 'rem' in request.GET:
                post_id = int(request.GET['post_id'])
                print(post_id)
                #quantity=int(request.GET['quantity'])
       
                removedpost = Cart.objects.get(id = post_id )
                removedpost.delete()'''
        
'''else:i_price=int(i_price)
            u=Cart(i_price=i_price,i_name=i_name)
            u.save()
            return HttpResponse('yes')
        '''
        
'''$('#i_price').val($('#iprice').html());
  $('#i_name').val($('#iname').html())'''    

def Cartie(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login first")
        return redirect("/Overdose/")
    else:
        hi=request.user
        s=Cart.objects.filter(author=hi)
        k=Cart.objects.filter(author=hi).aggregate(total=Sum(F('price')*F('quantity')))
        #f=Tprice.objects.get(author=hi)
        #g=f.tprice
        x=k['total']
        
        if x!=None:
            thank=True
        else:
            thank=False   
           
           
        cat={'cats':s,'price':x,'thank':thank}
        
         
       
        
        
        return render(request,'cartie.html',cat)  
        '''$('#number').each(function() {
  console.log($(this).text());
});

'''
def remove(request):
    wat=request.user
    if request.method=='GET':
        post_id = request.GET['post_id']
        
        #quantity=int(request.GET['quantity'])
        removedpost = Cart.objects.get(id = post_id )
        d=removedpost.price
        removedpost.delete()
        '''w=Tprice.objects.get(author=wat)
        h=w.tprice
        
        h=h-d
        
        Tprice.objects.filter(author=wat).update(tprice=h)'''
            
        return HttpResponse('success')

def removeorder(request):
    if request.method=='GET':
        cancel_id = request.GET['cancel_id']
        
        #quantity=int(request.GET['quantity'])
        removedorder = Order.objects.get(order_id = cancel_id )
        std=removedorder.slottime
        std=str(std)
        a=std.split('-')
        d=a[0]
        f=Slot.objects.get(start_time=d)
        g=f.id
        h=f.seats
        if h==0:
            Slot.objects.filter(id=g).update(available=True)
     
        h=h+1
        Slot.objects.filter(id=g).update(seats=h)
        Order.objects.filter(order_id=cancel_id).update(cancel="Cancel")
        return HttpResponse('success')
  
        
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from phone_field import PhoneField



# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    available=models.BooleanField(default=True)
    price=models.IntegerField()

    def __str__(self):
        return self.item_name    

#class Cart(models.Model):
    #items = models.ManyToManyField(Item)
    #author=models.ForeignKey(User,on_delete=models.CASCADE)        

#created_date = models.DateTimeField(default=timezone.now)    
place=(
    ("hostel_delivery","hostel_delivery"),
    ("meal_at_overdose","meal_at_overdose"),
)

class Slot(models.Model):
    choice=models.CharField(max_length=20,choices=place,default="hostel_delivery")
    date=models.DateField(default=datetime.date.today)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    available=models.BooleanField(default=True)
    seats=models.PositiveIntegerField(default=10,validators=[MaxValueValidator(10),MinValueValidator(0)])

   
    def __str__(self):
        return '%s-%s' % (self.start_time, self.end_time)

class Cart(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,default=None,blank=True)
    price=models.PositiveIntegerField(default=0)
    quantity=models.PositiveIntegerField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None,blank=True)

    def __str__(self):
        return str(self.author)      

'''class Tprice(models.Model):
    tprice=models.PositiveIntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True,blank=True)     

    def __str__(self):
        return str(self.author)'''
stat=(
    ("Confirmed","Confirmed"),
    ("Not_Confirmed","Not_Confirmed"),
)
can=(
    ("Cancel","Cancel_by_user"),
)
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items=models.TextField()
    amount=models.PositiveIntegerField(null=False)
    slottime=models.ForeignKey(Slot,on_delete=models.CASCADE,default=None,blank=True)
    OrderBy=models.ForeignKey(User,on_delete=models.CASCADE,default=None,blank=True)
    placed=models.DateTimeField(default=timezone.now)
    delivery=models.CharField(max_length=25,choices=place)
    paid=models.BooleanField(default=False)
    status=models.CharField(max_length=25,choices=stat,default="None")
    cancel=models.CharField(max_length=25,choices=can,default="None")

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70 )
    order_id=models.PositiveIntegerField()
    desc = models.CharField(max_length=500)

class Phone(models.Model):
    phone=PhoneField(blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None,blank=True)


    

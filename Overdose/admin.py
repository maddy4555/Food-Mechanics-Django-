from django.contrib import admin
from .models import Item,Slot,Cart,Order,Contact,Phone
from django.contrib import messages 
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display=('item_name','category','subcategory','available','price')

    def make_available(modeladmin,request,queryset):
        queryset.update(available=True)
    def make_unavailable(modeladmin,request,queryset):
        queryset.update(available=False)

    admin.site.add_action(make_available, "Make available")
    admin.site.add_action(make_unavailable, "Make Unavailable")


admin.site.register(Item,ItemAdmin)
admin.site.register(Slot)
admin.site.register(Cart)

class OrderAdmin(admin.ModelAdmin): 
    list_display = ('order_id', 'amount', 'OrderBy','slottime','placed','delivery','paid','status','cancel') 
    #actions = ['make_Confirmed']
    def make_Confirmed(modeladmin, request, queryset): 
        queryset.update(status = 'Confirmed') 
        messages.success(request, "Selected Record(s) Marked as Confirmed Successfully !!") 
  
    def make_Not_Confirmed(modeladmin, request, queryset): 
        queryset.update(status = 'Not_Confirmed') 
        messages.success(request, "Selected Record(s) Marked as Not_Confirmed Successfully !!") 

    def make_paid(modeladmin,request,queryset):
        queryset.update(paid=True)
    def make_unpaid(modeladmin,request,queryset):
        queryset.update(paid=False)    
  
    admin.site.add_action(make_Confirmed, "Make Confirmed") 
    admin.site.add_action(make_Not_Confirmed, "Make Not_Confirmed") 
    admin.site.add_action(make_paid, "Make Paid")
    admin.site.add_action(make_unpaid, "Make Unpaid") 
#show_average.short_description = "Average"

admin.site.register(Order,OrderAdmin)  
#admin.site.register(Tprice)
class ContactAdmin(admin.ModelAdmin):
    list_display=('msg_id','name','email','phone','order_id','desc')
admin.site.register(Contact,ContactAdmin)

class PhoneAdmin(admin.ModelAdmin):
    list_display=['phone','author']

admin.site.register(Phone,PhoneAdmin)



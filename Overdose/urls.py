from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('southindian/',views.southindian,name='southindian'),
    path('italian/',views.italian,name='italian'),
    path('chinese/',views.chinese,name='chinese'),
    path('bakery/',views.bakery,name='bakery'),
    path('savouries/',views.savouries,name='savouries'),
    path('indian/',views.indian,name='indian'),
    path('drinks/',views.drinks,name='drinks'),
    path('icecream/',views.icecream,name='icecream'),
    path('breads/',views.breads,name='breads'),
    path('orders/',views.orders,name='orders'),
    path('reservation/',views.reservation,name='reservation'),
    path('feedback/',views.feedback,name='feedback'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/',views.cart,name='cart'), 
    path('Cartie/',views.Cartie,name='Cartie'),   
    path('logout/',views.logout,name='logout'),
    path('remove/',views.remove,name='remove'),
    path('thankyou/',views.thank,name='thank'),
    path('removeorder/',views.removeorder,name='removeorder'),
]


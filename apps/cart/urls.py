from django.urls import path
from . import views
from apps.cart.webhook import webhook


app_name = 'cart'
urlpatterns = [
    path('cart', views.Cart_Detail, name='cartView'),
    path('cart/success', views.Success, name='successView'),
    path('hooks/', webhook, name='webHook'),

]

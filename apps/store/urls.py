from django.urls import path, include
from . import views, api
from apps.coupon.api import api_can_use
from apps.newsletter.api import api_add_subscriber

app_name = 'store'
urlpatterns = [
    path('search/', views.Search, name='searchView'),

    # API
    path('api/create_checkout_session/', api.create_checkout_session, name='create_checkout_session'),
    path('api/add_to_cart/', api.api_add_to_cart, name='api_add_to_card'),
    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/remove_from_cart/', api.api_remove_from_cart, name='api_remove_from_cart'),
    path('api/checkout/', api.api_checkout, name='api_checkout'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),


    path('<slug:category_slug>/<slug:slug>/', views.ProductDetail, name= 'productDetail'),
    path('<slug:slug>/', views.CategoryDetail, name= 'categoryDetail'),

]

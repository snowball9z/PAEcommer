from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Frontpage, name='frontpage'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
]

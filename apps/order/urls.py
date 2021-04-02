from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('admin/admin_order_pdf/<int:order_id>/', views.admin_order_pdf, name='admin_order_pdf'),
]

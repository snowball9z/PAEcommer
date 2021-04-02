from django.urls import path
from . import views as userView
from django.contrib.auth import views

app_name = 'userprofile'
urlpatterns = [
    path('myaccount/', userView.myaccount, name='accountView'),
    path('signup/', userView.signup, name='signupView'),
    path('logout/', views.LogoutView.as_view(), name='logoutView'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='loginView'),
]

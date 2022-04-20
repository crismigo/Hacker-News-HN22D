from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('login/', views.loginView, name="Login"),
    path('logout/', views.logoutView, name="Logout"),
]

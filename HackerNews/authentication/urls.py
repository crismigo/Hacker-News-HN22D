from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginView, name="Login"),
    path('callback', views.callBack, name="Callback"),
    path('logout/', views.logoutView, name="Logout"),
]

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.news,name="Home"),
    path('news/', views.news,name="News"),
    path('news/<int:page>', views.news,name="Newspage"),
    path('newest/', views.newest,name="Newest"),
    path('newest/<int:page>', views.newest,name="Newest"),
    path('ask/', views.ask,name="Ask"),
]
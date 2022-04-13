from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.news,name="News"),
    path('news/', views.news,name="News"),
    path('newest/', views.newest,name="Newest"),
    path('ask/', views.ask,name="Ask"),
]
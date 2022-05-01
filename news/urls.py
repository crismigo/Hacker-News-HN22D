from django.urls import path

from . import views

urlpatterns = [
    path('', views.news, name="Home"),
    path('news/', views.news, name="News"),
    path('newest/', views.newest, name="Newest"),
    path('ask/', views.ask, name="Ask"),
]

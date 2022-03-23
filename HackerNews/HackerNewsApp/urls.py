from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page, name='news_page')
]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:item_id>', views.view,name="ViewItem"),
    path('<int:item_id>/edit/', views.edit,name="EditItem"),
    path('create/', views.create,name="CreateItem"),
    path('<int:item_id>/delete/', views.delete,name="DeleteItem"),
]
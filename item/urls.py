from django.urls import path

from . import views

urlpatterns = [
    path('<int:item_id>', views.view, name="ViewItem"),
    path('<int:item_id>/edit/', views.edit, name="EditItem"),
    path('<int:item_id>/delete/', views.delete, name="DeleteItem"),
]

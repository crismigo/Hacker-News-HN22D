from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('submission/add', views.addSubmissionComment, name="AddSubmissionComment"),
    path('submission/edit', views.editSubmissionComment, name="EditSubmissionComment"),
    path('submission/remove', views.removeSubmissionComment, name="RemoveSubmissionComment"),
    path('comment/add', views.addReplyComment, name="AddComment2Comment"),
    path('comment/edit', views.editReplyComment, name="EditComment2Comment"),
    path('comment/remove', views.removeReplyComment, name="RemoveComment2Comment"),
]

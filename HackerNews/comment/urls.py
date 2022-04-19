from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('submission/<int:id_submission>', views.addSubmissionComment, name="AddSubmissionComment"),
    path('reply/<int:id_comment>', views.addReplyComment, name="AddComment2Comment"),
]

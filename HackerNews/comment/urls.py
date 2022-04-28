from django.urls import path

from . import views

urlpatterns = [
    path('submission/<int:id_submission>', views.addSubmissionComment, name="AddSubmissionComment"),
    path('reply/<int:id_comment>', views.addReplyComment, name="AddComment2Comment"),
]

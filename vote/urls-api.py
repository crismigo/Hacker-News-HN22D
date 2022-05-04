from django.urls import path, include

from vote.api import  VoteSubmissionApiView, VoteCommentApiView

urlpatterns = [
    path('submissions/<int:id>/', VoteSubmissionApiView.as_view()),
    path('comments/<int:id>/', VoteCommentApiView.as_view()),
]
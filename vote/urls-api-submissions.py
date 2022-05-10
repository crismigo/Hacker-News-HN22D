from django.urls import path, include

from vote.api import VoteSubmissionApiView

urlpatterns = [
    path('', VoteSubmissionApiView.as_view()),
]
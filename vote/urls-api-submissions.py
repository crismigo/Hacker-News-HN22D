from django.urls import path, include

from vote.api import VoteSubmissionApiView, CheckVoteSubmissionApiView

urlpatterns = [
    path('', VoteSubmissionApiView.as_view()),
    path('isVoted/', CheckVoteSubmissionApiView.as_view()),

]
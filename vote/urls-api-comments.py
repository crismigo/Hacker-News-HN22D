from django.urls import path, include

from vote.api import VoteCommentApiView, CheckVoteCommentApiView

urlpatterns = [
    path('', VoteCommentApiView.as_view()),
    path('isVoted/', CheckVoteCommentApiView.as_view()),
]
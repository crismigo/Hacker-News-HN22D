from django.urls import path, include

from vote.api import VoteCommentApiView

urlpatterns = [
    path('', VoteCommentApiView.as_view()),
]
from django.urls import path

from . import views

urlpatterns = [
    path('voteSubmission/<int:id>', views.vote_submission, name="voteSubmission"),
    path('unvoteSubmission/<int:id>', views.unvote_submission, name="unvoteSubmission"),
    path('voteComment/<int:idc>', views.vote_comment, name="voteComment"),
    path('unvoteComment/<int:idc>/', views.unvote_comment, name="unvoteComment"),
]

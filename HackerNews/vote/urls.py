from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('voteSubmission/<int:id>', views.vote_submission, name="voteSubmission"),
    path('unvoteSubmission/<int:id>', views.unvote_submission, name="unvoteSubmission"),
    path('voteComment/', views.vote_comment, name="voteComment"),
    path('unvoteComment/', views.unvote_comment, name="unvoteComment"),
]
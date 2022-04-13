from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('voteSubmission/', views.vote_submission, name="voteSubmission"),
    path('unvoteSubmission/', views.unvote_submission, name="unvoteSubmission"),
    path('voteComment/', views.vote_comment, name="voteComment"),
    path('unvoteComment/', views.unvote_comment, name="unvoteComment"),
]
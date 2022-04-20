from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:user_id>/', views.show, name="ShowProfile"),
    path('<int:user_id>/submissions/', views.submissions, name="ShowUserSubmissions"),
    path('<int:user_id>/upvotedsubmissions/', views.upvoted_submissions, name="UpvotedSubmissions"),
    path('<int:user_id>/upvotedComments/', views.upvoted_comments, name="UpvotedComments"),
]

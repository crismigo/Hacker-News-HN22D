from django.urls import path, include

from userProfile.api import UserGetUpdateProfile, UserThreads, UserOwnSubmissions, UserUpvotedSubmissions, \
    UserUpvotedComments

urlpatterns = [
    path('<int:user_id>/', UserGetUpdateProfile.as_view()),
    path('<int:user_id>/threads/', UserThreads.as_view()),
    path('<int:user_id>/submissions/', UserOwnSubmissions.as_view()),
    path('<int:user_id>/upvoted/submissions/', UserUpvotedSubmissions.as_view()),
    path('<int:user_id>/upvoted/comments/', UserUpvotedComments.as_view()),
]
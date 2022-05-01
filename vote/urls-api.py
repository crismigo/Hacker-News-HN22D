from django.urls import path, include

from vote.api import  VotesDetailApiView

urlpatterns = [
    path('<int:id>/', VotesDetailApiView.as_view()),
]
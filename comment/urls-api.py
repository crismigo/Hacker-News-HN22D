from django.urls import path, include
from .api import CommentDetailApiView

urlpatterns = [
    path('<int:comment_id>/', CommentDetailApiView.as_view()),
]

from django.urls import path, include
from .api import CommentDetailApiView, CommentToSubmissionDetailApiView, CommentToCommentDetailApiView

urlpatterns = [
    path('<int:comment_id>/', CommentDetailApiView.as_view()),
    path('reply/', CommentToCommentDetailApiView.as_view()),
    path('submission/', CommentToSubmissionDetailApiView.as_view())
]

from django.urls import path, include
from .api import CommentDetailApiView, CommentToSubmissionDetailApiView, CommentToCommentDetailApiView

urlpatterns = [
    path('<int:comment_id>/', CommentDetailApiView.as_view()),
    path('reply/<int:replied_comment_id>/', CommentToCommentDetailApiView.as_view()),
    path('submission/<int:submission_id>/', CommentToSubmissionDetailApiView.as_view())
]
from django.urls import path, include
from .api import CommentDetailApiView, CommentToSubmissionDetailApiView, CommentToCommentDetailApiView, \
    VoteCommentApiView

urlpatterns = [
    path('<int:comment_id>/', CommentDetailApiView.as_view()),
    path('reply/<int:replied_comment_id>/', CommentToCommentDetailApiView.as_view()),
    path('submission/<int:submission_id>/', CommentToSubmissionDetailApiView.as_view()),
    path('comments/<int:id>/vite', VoteCommentApiView.as_view()),
]
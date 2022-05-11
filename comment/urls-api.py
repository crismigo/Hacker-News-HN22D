from django.urls import path, include
from .api import CommentDetailApiView, CommentApiView

urlpatterns = [
    path('', CommentApiView.as_view()),
    path('<int:comment_id>/', CommentDetailApiView.as_view()),
    path('<int:id>/vote/', include("vote.urls-api-comments")),
]
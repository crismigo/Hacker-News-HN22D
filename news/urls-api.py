from django.urls import path, include
from .api import NewsApiView, NewsDetailApiView, NewsNewestApiView, NewsAskApiView

urlpatterns = [
    path('', NewsApiView.as_view()),
    path('<int:news_id>/', NewsDetailApiView.as_view()),
    path('newest/', NewsNewestApiView.as_view()),
    path('ask/', NewsAskApiView.as_view()),
    path('<int:id>/vote/', include('vote.urls-api-submissions')),
]
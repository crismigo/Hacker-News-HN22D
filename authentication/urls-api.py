from django.urls import path, include

from authentication.api import LoginCallback

urlpatterns = [
    path('callback/', LoginCallback.as_view()),
]
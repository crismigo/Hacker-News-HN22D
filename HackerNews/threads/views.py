from django.shortcuts import render

# Create your views here.
from authentication.models import User
from news.models import Comment


def viewThread(request, user_id):
    requested_user = User.objects.get(id=user_id)
    comments = Comment.objects.filter(user_id=user_id)
    return render(request, "threads.html", {"Comments": comments,"requestedUser":requested_user})

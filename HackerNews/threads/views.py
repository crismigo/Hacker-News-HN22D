from django.shortcuts import render

# Create your views here.
from news.models import Comment


def viewThread(request):
    comments = Comment.objects.filter(user=request.user)
    for comment in comments:
        print(comment)
        comment.timeSinceCreation()
    return render(request, "threads.html", {"comments": comments})

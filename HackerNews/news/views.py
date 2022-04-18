from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from news.models import Submission

def news(request,page=1):
    submission = Submission.objects.all().filter().annotate(points=Count('votes')).order_by('-points')[(page-1)*30:(page*30)]
    unvote ={}
    for subm in submission:
        unvote[subm.id] = subm.unvote(request.user)
    return render(request, "news.html",  {"Submissions": submission,"page": page+1,"unvote":unvote})

def newest(request,page=1):
    submission = Submission.objects.order_by('-created_at').filter()[(page-1)*30:(page*30)]
    # Setejo els domainurl de les submissions.

    return render(request, "news.html", {"Submissions": submission})


def ask(request):
    pass
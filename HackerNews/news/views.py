from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from news.models import Submission, SubmissionType


def news(request,page=1):
    #subm= Submission.objects.all().annotate(points=Count('votes')).order_by('-points')
    subm_paginator = Paginator(Submission.objects.order_by('-title'),30)
    pages = subm_paginator.page(1)
    submission = Submission.objects.all().filter().annotate(points=Count('votes')).order_by('-points')[(page-1)*30:(page*30)]

    return render(request, "news.html",  {"Submissions": submission,"page": page+1,"pages":pages,"subm_paginator":subm_paginator.count})

def newest(request,page=1):
    submission = Submission.objects.order_by('-created_at').filter()[(page-1)*30:(page*30)]
    # Setejo els domainurl de les submissions.
    return render(request, "newsest.html", {"Submissions": submission,"page":page+1})


def ask(request,page=1):
    type = SubmissionType.objects.get(name="ask")
    submission = Submission.objects.filter(type=type).annotate(points=Count('votes')).order_by('-points')[(page-1)*30:(page*30)]
    # Setejo els domainurl de les submissions.
    return render(request, "ask.html", {"Submissions": submission,"page":page+1})

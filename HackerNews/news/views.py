from django.shortcuts import render, redirect

# Create your views here.
from news.models import Submission


def hide(request,id):
    submission = Submission.objects.get(id=id)
    submission.hide = True # 1 Es un enter pero ho he deixat com boolea.
    submission.save()
    return redirect('/news')

def news(request):
    submission = Submission.objects.all().filter(hide=0).order_by('-points')[:30]

    for subm in submission:
        subm.timesincecreation()
        subm.domainurl()
    return render(request, "news.html",  {"Submissions": submission})

def newest(request):
    submission = Submission.objects.order_by('-created_at').filter(hide=0)[:30]
    # Setejo els domainurl de les submissions.
    for subm in submission:
        subm.timesincecreation()
        subm.domainurl()
    return render(request, "news.html", {"Submissions": submission})


def ask(request):
    pass
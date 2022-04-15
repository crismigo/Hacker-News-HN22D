from django.shortcuts import render

# Create your views here.
from news.models import Submission

def news(request):

    submission = Submission.objects.order_by('-points').all()[:30]
    #Setejo els domainurl de les submissions.
    for subm in submission:
        subm.timesincecreation()
        subm.domainurl()
    return render(request, "news.html",  {"Submissions": submission})

def newest(request):
    pass

def ask(request):
    pass
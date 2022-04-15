from django.shortcuts import render

# Create your views here.
from news.models import Submission

def news(request):

    #submission = Submission.objects.all()
    #return render(request, "news.html",  {"Submissions": submission})
    return render(request, "news.html")

def newest(request):
    pass

def ask(request):
    pass
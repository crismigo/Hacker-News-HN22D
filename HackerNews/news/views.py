from django.shortcuts import render

# Create your views here.
from news.models import Submission


def news(request):
    return render(request, "news.html")

def newest(request):
    pass

def ask(request):
    pass
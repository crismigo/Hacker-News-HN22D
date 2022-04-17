from urllib.parse import urlparse

from django.shortcuts import render, redirect


# Create your views here.
from news.models import Submission, SubmissionType
from submit.forms import SubmissionForm


def view(request, item_id):
    pass

def create(request):
    if request.method=="POST":
        formulario = SubmissionForm(data=request.POST)
        if formulario.is_valid():
            title= request.POST.get("title")
            url = request.POST.get("url")
            text = request.POST.get("text")
            type=SubmissionType.objects.get(name="url")
            user=request.user
            if url!="":
                submission=Submission(title=title,type=type,author=user,url=url,text="",points=1)
                submission.save()
                if text!="":
                    pass
                print(submission)
                return redirect("/")

            if text!="":
                pass

            formulario.url.errors="prova"
            return redirect("/submit", {"form_error":formulario})
    return redirect("/submit")

def edit(request,item_id):
    pass

def delete(request,item_id):
    pass
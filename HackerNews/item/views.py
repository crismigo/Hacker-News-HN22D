from urllib.parse import urlparse

from django.shortcuts import render, redirect


# Create your views here.
from news.models import Submission
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
            type="url"
            user=request.user
            if url!="":
                submission=Submission(title,type,user,url,"")
                if text!="":
                    pass
                print(submission)
                redirect("/")


            redirect("/submit", {"form_error":formulario})
    redirect("/submit")

def edit(request,item_id):
    pass

def delete(request,item_id):
    pass
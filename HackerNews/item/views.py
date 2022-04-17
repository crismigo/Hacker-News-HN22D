from urllib.parse import urlparse

from django.shortcuts import render, redirect


# Create your views here.
from news.models import Submission, SubmissionType
from submit.forms import SubmissionForm


def view(request, item_id):
    pass

def edit(request,item_id):
    pass

def delete(request,item_id):
    pass
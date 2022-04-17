from django.shortcuts import render, redirect

from news.models import Submission
from .forms import SubmissionForm


# Create your views here.
def submissionView(request, errorForm=""):
    if request.user.is_authenticated:
        if errorForm == "":
            submission_form = SubmissionForm()
        else:
            submission_form = errorForm
        return render(request, "submit.html", {"form": submission_form})

    else:
        return redirect("/login")


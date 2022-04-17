from django.shortcuts import render
from .forms import SubmissionForm


# Create your views here.
def submissionView(request, errorForm=""):
    if errorForm == "":
        submission_form = SubmissionForm()
    else:
        submission_form = errorForm
    return render(request, "submit.html", {"form": submission_form})

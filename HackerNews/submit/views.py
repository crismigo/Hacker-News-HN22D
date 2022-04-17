from django.shortcuts import render, redirect

from comment.models import Comment, ActionType
from news.models import Submission, SubmissionType
from .forms import SubmissionForm


# Create your views here.
def submissionView(request):
    if request.user.is_authenticated:
        submission_form = SubmissionForm()
        if request.method == "POST":
            submission_form = SubmissionForm(data=request.POST)
            if submission_form.is_valid():
                title = request.POST.get("title")
                url = request.POST.get("url")
                text = request.POST.get("text")
                type = SubmissionType.objects.get(name="url")
                user = request.user
                if url != "":
                    submission = Submission(title=title, type=type, author=user, url=url, points=1)
                    submission.save()
                    if text != "":
                        type_comment=ActionType.objects.get(name="Submission")
                        comment = Comment(submission=submission,type=type_comment,user=user)
                        comment.save()
                    return redirect("/")

                if text != "":
                    pass
        return render(request, "submit.html", {"form": submission_form})
    else:
        return redirect("/login")


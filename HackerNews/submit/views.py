from django.shortcuts import render, redirect

from news.models import Submission, SubmissionType, Comment, ActionType, Vote
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

                user = request.user
                if url != "":
                    submision_type = SubmissionType.objects.get(name="url")
                    submission = Submission(title=title, type=submision_type, author=user, url=url)
                    submission.save()

                    action_type = ActionType.objects.get(name="Submission")
                    vote = Vote(submission=submission, type=action_type, user=user)
                    vote.save()

                    if text != "":
                        comment = Comment(submission=submission, type=action_type, user=user, text=text)
                        comment.save()

                        action_type = ActionType.objects.get(name="Comment")
                        vote = Vote(submission=comment, type=action_type, user=user)
                        vote.save()

                    return redirect("/")

                if text != "":
                    submision_type = SubmissionType.objects.get(name="ask")
                    submission = Submission(title=title, type=submision_type, author=user, text=text)
                    submission.save()

                    action_type = ActionType.objects.get(name="Submission")
                    vote = Vote(submission=submission, type=action_type, user=user)
                    vote.save()

                    return redirect("/")

        return render(request, "submit.html", {"form": submission_form})
    else:
        return redirect("/login")

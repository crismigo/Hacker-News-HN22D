from django.shortcuts import render, redirect

# Create your views here.
from item.forms import ShowSubmissionComment
from news.models import Submission,  Comment, Vote
from .forms import EditForm


def view(request, item_id):
    submission = Submission.objects.get(id=item_id)
    commentForm = ShowSubmissionComment
    return render(request, "viewItem.html", {"submission": submission, "form": commentForm})


def edit(request, item_id):
    if request.user.is_authenticated:
        submission = Submission.objects.get(id=item_id)
        submission_form = EditForm(instance=submission)
        if request.method == "POST":
            submission_form = EditForm(data=request.POST)
            if submission_form.is_valid():
                submission = Submission.objects.get(id=item_id)
                submission.title = request.POST.get("title")
                submission.text = request.POST.get("text")
                submission.save()
                return redirect("/item/" + str(item_id))

        return render(request, "editItem.html", {"submission": submission, "form": submission_form})
    else:
        return redirect("Login")


def deleteComments(comment):
    sub_comments = Comment.objects.filter(replied_comment=comment)
    for sub_comment in sub_comments:
        deleteComments(sub_comment)

    Vote.objects.filter(comment=comment).delete()
    comment.delete()


def delete(request, item_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST["yes"]:
                submission = Submission.objects.get(id=item_id)
                if submission != None:
                    comments = Comment.objects.filter(submission=submission)
                    for comment in comments:
                        deleteComments(comment)
                    Vote.objects.filter(submission=submission).delete()
                    submission.delete()
                    return redirect("/")
            else:
                return redirect("/item/" + str(item_id))

        submission = Submission.objects.get(id=item_id)
        return render(request, "deleteItem.html", {"submission": submission})
    else:
        return redirect("Login")

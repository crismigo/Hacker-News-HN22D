from django.shortcuts import render, redirect


# Create your views here.
from item.forms import ShowSubmissionComment
from news.models import Comment, ActionType


def addSubmissionComment(request,id_submission):
    if request.user.is_authenticated:
        if request.method == "POST":
            commentForm = ShowSubmissionComment(data=request.POST)
            if commentForm.is_valid():
                comment = request.POST.get("comment")
                sub_type=ActionType.objects.get(name="Submission")
                newComment=Comment(submission_id=id_submission,type=sub_type,user=request.user,text=comment)
                newComment.save()
                return redirect("ViewItem",id_submission)
        return redirect("ViewItem",id_submission)
    else:
        return redirect("Login")


def editSubmissionComment(request):
    pass


def removeSubmissionComment(request):
    pass


def addReplyComment(request):
    pass


def editReplyComment(request):
    pass


def removeReplyComment(request):
    pass
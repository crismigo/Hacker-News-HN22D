from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from comment.models import ActionType, Comment
from item.forms import ShowSubmissionComment


def addSubmissionComment(request, id_submission):
    try:
        if request.user.is_authenticated:
            if request.method == "POST":
                commentForm = ShowSubmissionComment(data=request.POST)
                if commentForm.is_valid():
                    comment = request.POST.get("comment")
                    sub_type = ActionType.objects.get(name="Submission")
                    newComment = Comment(submission_id=id_submission, type=sub_type, user=request.user, text=comment)
                    newComment.save()
                    return redirect("ViewItem", id_submission)
            return redirect("ViewItem", id_submission)
        else:
            return redirect("Login")
    except:
        return HttpResponseNotFound('<h1>Submission not found</h1>')


def getSubmissionFromComment(id_comment):
    try:
        comment = Comment.objects.get(id=id_comment)
        if comment.type.name == "Submission":
            return comment.submission.id
        else:
            return getSubmissionFromComment(comment.replied_comment_id)
    except:
        return HttpResponseNotFound('<h1>Comment not found</h1>')


def addReplyComment(request, id_comment):
    try:
        if request.user.is_authenticated:
            if request.method == "POST":
                commentForm = ShowSubmissionComment(data=request.POST)
                if commentForm.is_valid():
                    comment = request.POST.get("comment")
                    com_type = ActionType.objects.get(name="Comment")
                    newComment = Comment(replied_comment_id=id_comment, type=com_type, user=request.user, text=comment)
                    newComment.save()
                    submission_id = getSubmissionFromComment(id_comment)
                    return redirect("ViewItem", submission_id)
            commentForm = ShowSubmissionComment()
            comment = Comment.objects.get(id=id_comment)
            return render(request, "replyComment.html", {"form": commentForm, "comment": comment})
        else:
            return redirect("Login")
    except:
        return HttpResponseNotFound('<h1>Comment not found</h1>')

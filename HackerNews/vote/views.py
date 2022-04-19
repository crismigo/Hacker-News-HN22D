from django.shortcuts import redirect


# Create your views here.
from news.models import Submission, Vote, ActionType, Comment


def vote_submission(request, id):
    if request.user.is_authenticated:
        subm = Submission.objects.get(id=id)
        subm.points+=1
        subm.save()
        act = ActionType.objects.get(name="Submission")
        vote = Vote.objects.get_or_create(submission=subm,user=request.user,type=act)
        if vote :
            print("correct")
        else :
            print("incorrect")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("Login")


def unvote_submission(request, id):
    if request.user.is_authenticated:
        subm = Submission.objects.get(id=id)
        subm.points -= 1
        subm.save()
        act = ActionType.objects.get(name="Submission")
        Vote.objects.get(submission=subm,user=request.user,type=act).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("Login")


def vote_comment(request,idc):
    if request.user.is_authenticated:
        comm = Comment.objects.get(id=idc)
        act = ActionType.objects.get(name="Comment")
        vote = Vote.objects.get_or_create(comment=comm, user=request.user, type=act)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("Login")




def unvote_comment(request,idc):
    if request.user.is_authenticated:
        comm = Comment.objects.get(id=idc)
        act = ActionType.objects.get(name="Comment")
        Vote.objects.get(comment=comm, user=request.user,type=act).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("Login")

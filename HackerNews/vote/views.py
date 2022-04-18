from django.shortcuts import redirect


# Create your views here.
from news.models import Submission, Vote, ActionType


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
        return redirect("/login")


def unvote_submission(request, id):
    subm = Submission.objects.get(id=id)
    subm.points -= 1
    subm.save()

    Vote.objects.get(submission=subm,user=request.user).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def vote_comment(request):
    pass


def unvote_comment(request):
    pass
